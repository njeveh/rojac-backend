# Generated by Django 4.1.1 on 2023-02-20 09:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0002_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="C2bBillRefNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bill_ref_number", models.CharField(max_length=12)),
                ("amount", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="C2BPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "TransactionType",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("TransID", models.CharField(blank=True, max_length=12, null=True)),
                ("TransTime", models.CharField(blank=True, max_length=25, null=True)),
                ("TransAmount", models.CharField(blank=True, max_length=12, null=True)),
                (
                    "BusinessShortCode",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                (
                    "BillRefNumber",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "InvoiceNumber",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "OrgAccountBalance",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                (
                    "ThirdPartyTransID",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("MSISDN", models.CharField(blank=True, max_length=100, null=True)),
                ("FirstName", models.CharField(blank=True, max_length=20, null=True)),
                ("MiddleName", models.CharField(blank=True, max_length=20, null=True)),
                ("LastName", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("phone_number", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_title", models.CharField(max_length=150)),
                ("slug", models.SlugField(default="")),
                ("product_description", models.TextField()),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=100,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("product_main_image", models.ImageField(upload_to="images/products")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_featured", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="cat_imgs/")),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="ProductVariation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.CharField(max_length=120, unique=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("size", "Size"),
                            ("quantity", "Quantity"),
                            ("package", "Package"),
                        ],
                        default=("size", "Size"),
                        max_length=120,
                    ),
                ),
                ("image", models.ImageField(upload_to="product/images/")),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=100,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("number_in_stock", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rojac.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductVariationImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="product/images/")),
                ("is_featured", models.BooleanField(default=False)),
                ("is_thumbnail", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "product_variation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rojac.productvariation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="product/images/")),
                ("is_featured", models.BooleanField(default=False)),
                ("is_thumbnail", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rojac.product"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="product_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rojac.productcategory"
            ),
        ),
    ]
