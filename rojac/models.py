from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL, PROTECT
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser

# make email in User a mandatory field
User._meta.get_field('email')._unique = True
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


class Commodity(models.Model):
    """a model representation of a rojac sale item"""

    # commodity category options
    options = (
        ('bones and joints', 'Bones and Joints'),
        ('digestive', 'Digestive'),
        ('cardiovascular', 'Cardiovascular'),
        ('imune boosters', 'Imune Boosters'),
        ('men health', 'Men Health'),
        ('beauty and longevity', 'Beauty and Longevity'),
        ('suma living', 'Suma Living'),
    )
    commodity_name = models.CharField(max_length=150, null=False)
    category = models.CharField(
        max_length=60, choices=options, default='others')
    description = models.TextField(null=False)
    price = models.FloatField(null=False)
    pricing_unit = models.CharField(max_length=60, null=False)
    number_in_stock = models.IntegerField(null=True)
    commodity_main_image = models.ImageField(
        upload_to='images/commodities', null=False)
    commodity_extra_image1 = models.ImageField(
        upload_to='images/commodities', null=True)
    commodity_extra_image2 = models.ImageField(
        upload_to='images/commodities', null=True)

    def __str__(self):
        """returns the name of a commodity as its string representation"""
        return self.commodity_name


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
#     order_items = models.ManyToManyField(Commodity)
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
