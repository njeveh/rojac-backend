# Generated by Django 4.1.1 on 2023-02-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rojac", "0003_alter_product_product_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(
                default=models.CharField(max_length=150, unique=True)
            ),
        ),
    ]
