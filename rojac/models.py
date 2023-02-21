import unicodedata
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL, PROTECT
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator

# make email in User a mandatory field
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class Client(models.Model):
    """a model representation of a rojac client data"""
    profile = models.OneToOneField(
        User, on_delete=CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15, null=False)

    def __str__(self):
        """method returns a string representation of a client instance"""
        return self.profile.username
    # product category options
    options = (
        ('bones and joints', 'Bones and Joints'),
        ('digestive', 'Digestive'),
        ('cardiovascular', 'Cardiovascular'),
        ('imune boosters', 'Imune Boosters'),
        ('men health', 'Men Health'),
        ('beauty and longevity', 'Beauty and Longevity'),
        ('suma living', 'Suma Living'),
    )


class ProductCategory(models.Model):
    category_title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural = 'Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.category_title


class Product(models.Model):
    """a model representation of a rojac sale item"""

    product_title = models.CharField(max_length=150, null=False, unique=True)
    slug = models.SlugField(default="", null=False)
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    product_description = models.TextField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=50,
                                validators=[MinValueValidator(0)], null=True, blank=True)
    product_main_image = models.ImageField(
        upload_to='product/inages', null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        """returns the name of a product as its string representation"""
        return self.product_title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images/')
    is_featured = models.BooleanField(default=False)
    is_thumbnail = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return ''.join([self.product.product_title, ' (image #', unicodedata(self.id), ') '])


VARIATION_CATEGORIES = (
    ('size', 'Size'),
    ('quantity', 'Quantity'),
    ('package', 'Package'),
)


class ProductVariationManager(models.Manager):
    def all(self):
        return super(ProductVariationManager, self).filter(is_featured=True)

    def all_sizes(self):
        return self.all().filter(category='size')

    def all_quantities(self):
        return self.all().filter(category='quantity')

    def all_packages(self):
        return self.all().filter(category='package')

    def variation_by_category(self):
        return [(category[0], self.filter(category=category[0])) for category in VARIATION_CATEGORIES]


class ProductVariation(models.Model):
    """A variation on a particular product"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=120, unique=True)
    category = models.CharField(
        max_length=120, choices=VARIATION_CATEGORIES, default=VARIATION_CATEGORIES[0])
    image = models.ImageField(upload_to='product/images/')
    price = models.DecimalField(decimal_places=2, max_digits=50,
                                validators=[MinValueValidator(0)], null=True, blank=True)
    number_in_stock = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False,)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_featured = models.BooleanField(default=False)

    objects = ProductVariationManager()

    def __unicode__(self):
        return ' | ' + self.title + ' | <' + self.category + '> of ' + self.product.title


class ProductVariationImage(models.Model):
    product_variation = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images/')
    is_featured = models.BooleanField(default=False)
    is_thumbnail = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return ''.join([self.product_variation.product.product_title, ' (image #', unicodedata(self.id), ') '])

# class LNMOnline(models.Model):
#     CheckoutRequestID = models.CharField(max_length=50, blank=True, null=True)
#     MerchantRequestID = models.CharField(max_length=20, blank=True, null=True)
#     ResultCode = models.IntegerField(blank=True, null=True)
#     ResultDesc = models.CharField(max_length=120, blank=True, null=True)
#     Amount = models.FloatField(blank=True, null=True)
#     MpesaReceiptNumber = models.CharField(max_length=15, blank=True, null=True)
#     Balance = models.CharField(max_length=12, blank=True, null=True)
#     TransactionDate = models.DateTimeField(blank=True, null=True)
#     PhoneNumber = models.CharField(max_length=13, blank=True, null=True)

#     def __str__(self):
#         return f"{self.PhoneNumber} >> {self.Amount} >> {self.MpesaReceiptNumber}"


# class LNMOrder(models.Model):
#     order_items = models.ManyToManyField(Product)
#     date_placed = models.DateTimeField(default=datetime.now, null=True)
#     order_value = models.FloatField(null=False)
#     is_delivered = models.BooleanField(default=False, null=False)
#     date_delivered = models.DateTimeField(null=True)
#     payment_transaction = models.ForeignKey(
#         LNMOnline, on_delete=PROTECT, null=False)
#     placer = models.ForeignKey(Client, on_delete=SET_NULL, null=True)
#
#     transaction_id = models.CharField(max_length=15, blank=True, null=True)
class C2BPayment(models.Model):
    TransactionType = models.CharField(max_length=12, blank=True, null=True)
    TransID = models.CharField(max_length=12, blank=True, null=True)
    TransTime = models.CharField(max_length=25, blank=True, null=True)
    TransAmount = models.CharField(max_length=12, blank=True, null=True)
    BusinessShortCode = models.CharField(max_length=6, blank=True, null=True)
    BillRefNumber = models.CharField(max_length=20, blank=True, null=True)
    InvoiceNumber = models.CharField(max_length=20, blank=True, null=True)
    OrgAccountBalance = models.CharField(max_length=12, blank=True, null=True)
    ThirdPartyTransID = models.CharField(max_length=20, blank=True, null=True)
    MSISDN = models.CharField(max_length=100, blank=True, null=True)
    FirstName = models.CharField(max_length=20, blank=True, null=True)
    MiddleName = models.CharField(max_length=20, blank=True, null=True)
    LastName = models.CharField(max_length=20, blank=True, null=True)


class C2bBillRefNumber(models.Model):
    bill_ref_number = models.CharField(
        max_length=12, blank=False, null=False)
    amount = models.CharField(max_length=12, blank=False, null=False)


# class SavedOrder(models.Model):

#     order_items = models.ManyToOneRel(Product)
#     date_saved = models.DateTimeField(default=datetime.now, null=True)
#     order_value = models.FloatField(null=False)
#     placer = models.ForeignKey(Client, on_delete=SET_NULL, null=True)


# class Order(models.Model):
#     # delivery status options
#     delivery_status_options = (
#         ('in progress', 'In Progress'),
#         ('pending', 'Pending'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     )
#     # transaction status options
#     transaction_status_options = (
#         ('open', 'Open'),
#         ('closed', 'Closed'),
#         ('cancelled', 'Cancelled'),
#     )
#     order_items = models.ManyToOneRel(Product)
#     date_placed = models.DateTimeField(default=datetime.now, null=True)
#     order_value = models.FloatField(null=False)
#     delivery_status = models.CharField(
#         max_length=20, choices=delivery_status_options, default='pending')
#     transaction_status = models.CharField(
#         max_length=20, choices=transaction_status_options, default='open')
#     date_delivered = models.DateTimeField(null=True)
#     payment_transaction = models.ForeignKey(
#         C2BPayment, on_delete=PROTECT, null=False)
#     placer = models.ForeignKey(Client, on_delete=SET_NULL, null=True)

#     transaction_id = models.CharField(max_length=15, blank=True, null=True)
