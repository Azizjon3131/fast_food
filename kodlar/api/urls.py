from django.urls import path
from api.catalog.views import (ProductView, Category_ParentViews,Category_ChildViews,
                      TypeViews,ProductViews,Product_imageViews,CategoryViews,Product1Views)
from api.user.views import UserViews


app_name='api'
urlpatterns = [
    path('category/', CategoryViews.as_view()),
    path('product/', Product1Views.as_view()),

    path('category-list1/', Category_ParentViews.as_view()),
    path('category-list2/', Category_ChildViews.as_view()),
    path('category-type/', TypeViews.as_view()),
    path('category-product/', ProductViews.as_view()),
    path('category-image/', Product_imageViews.as_view()),
    path('user/', UserViews.as_view()),



    # path('category-list/',CategoryListGeneric.as_view()),
    # path('category-create/',CategoryCreateGeneric.as_view()),
    # path('category-list-create/',CategoryListCreateGeneric.as_view()),
    # path('category-reatrive/<int:pk>',CaregoryRetriveView.as_view()),
    # path('category-update/<int:pk>',CategoryUpdateView.as_view()),
    # path('category-update-retrieve/<int:pk>',CategoryRetrieveUpdateView.as_view()),
    # path('category-delete/<int:pk>',CategoryDestroyView.as_view()),
    # path('category-delete-retrieve/<int:pk>',CategoryRetriveDestroyView.as_view()),

    path('product/',ProductView.as_view()),

]
