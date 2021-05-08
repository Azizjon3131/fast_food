from django.contrib import admin
from .models import Category,Product,Product_type,Product_image
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','sort_order',]

class Product_imageAdmin(admin.TabularInline):
    model=Product_image
    fields=['image','is_main']
    extra=2

class Product_typeAdmin(admin.ModelAdmin):
    list_display=['name']

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category']
    inlines=[
        Product_imageAdmin
    ]
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product_type,Product_typeAdmin)
admin.site.register(Product,ProductAdmin)
