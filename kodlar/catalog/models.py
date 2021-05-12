from django.db import models



class Orders(models.Model):
    location=models.CharField(max_length=60,null=True,blank=True)
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    price_all=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.phone_number

class Orders_product(models.Model):
    orders=models.ForeignKey(Orders, on_delete=models.CASCADE)
    price = models.IntegerField()
    prise = models.IntegerField()
    product_name = models.CharField(max_length=40)
    user_id = models.IntegerField()


    def __str__(self):
        return self.product_name








class Category(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=30)
    parent =  models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    sort_order=models.IntegerField()

    def __str__(self):
        return self.name

class Product_type(models.Model):
    name=models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.name


class Product_image(models.Model):
    image=models.ImageField(upload_to='images')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    is_main=models.BooleanField()
