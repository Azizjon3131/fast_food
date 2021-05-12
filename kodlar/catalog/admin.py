from django.contrib import admin
from .models import Category,Product,Product_type,Product_image,Orders_product,Orders
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','sort_order',]

class Orders_productAdmin(admin.TabularInline):
    model = Orders_product
    fields = ['price','prise','product_name','user_id']

class OrdersAdmin(admin.ModelAdmin):
    fields = ['phone_number', 'price_all']
    inlines = [
        Orders_productAdmin
    ]


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

admin.site.register(Orders_product)
admin.site.register(Orders,OrdersAdmin)
