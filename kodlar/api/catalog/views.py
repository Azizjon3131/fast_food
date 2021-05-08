from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializer import CategorySerializer,ProductSerializer,Product_typeSerializer,Product_imageSerializer
from catalog.models import Category,Product,Product_type,Product_image

class Category_ParentViews(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        queryset=queryset.filter(parent_id=None)

        return queryset



class Category_ChildViews(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        id=self.request.query_params.get('id')
        print("mana id", id)
        queryset=queryset.filter(parent_id=id)

        return queryset



class TypeViews(generics.ListAPIView):
    serializer_class = Product_typeSerializer

    def get_queryset(self):
        queryset = Product_type.objects.all()
        id=self.request.query_params.get('id')
        print("mana id", id)
        queryset=queryset.filter(id=id)

        return queryset


class ProductViews(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id=self.request.query_params.get('id')
        print("mana id", id)
        queryset=queryset.filter(category_id=category_id)

        return queryset

class Product_imageViews(generics.ListAPIView):
    serializer_class = Product_imageSerializer

    def get_queryset(self):
        queryset = Product_image.objects.all()
        product_id=self.request.query_params.get('id')
        print("mana id", id)
        queryset=queryset.filter(product_id=product_id)

        return queryset













class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer(queryset)




class CategoryView(APIView):

    #bu aynan qaysidir malumotni olish uchun

    # def get(self, request, format=None):
    #
    #     categories = [category.name for category in Category.objects.all()]
    #     return Response(categories)

    #Bu hamma malumotlarni olish
    def list(self,request):
        queryset=Category.objects.all()
        serializer=CategoriSerializer(queryset)
        return Response(serializer.data)


    def post(self, request):
        print('keldimku')
        serializer=CategoriSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = serializer.create(serializer.data)
        serializer = CategoriSerializer(category)
        return Response(serializer.data)




#get
class CategoryListGeneric(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#create
class CategoryCreateGeneric(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#get and create
class CategoryListCreateGeneric(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


#Bu aynan bitta malumot turini oladi yani id=5 bolgan mahsulotni
class CaregoryRetriveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Put yani update
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Bunda ham retrive aynan bitta malumotni o'qib olinadi va uni o'zgartiriladi
#Retrieve and update
class CategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Aynan bitta malumotni o'chirish
#Delete
class CategoryDestroyView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Bu yerda ham o'qib olyapti retrieve qilib ham o'chiryapti
#retrieve and Delete
class CategoryRetriveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductView(APIView):

    def get(self, request, format=None):

        products = [product.name for product in Product.objects.all()]
        return Response(products)



    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.create(serializer.data)
        serializer = CategorySerializer(product)
        return Response(serializer.data)
