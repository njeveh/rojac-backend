from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    # list_display = ['title', 'price', 'active', 'updated_at']
    # list_editable = ['active', 'price']
    # list_filter = ['price', 'active', 'updated_at']
    # readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('product_title',)}

    class Meta():
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    class Meta():
        model = ProductImage


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'image_tag')


admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVariation)
admin.site.register(ProductVariationImage)


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(C2BPayment)
admin.site.register(C2bBillRefNumber)
