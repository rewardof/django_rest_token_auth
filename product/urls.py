from django.urls import path, include

from product import views

urlpatterns = [
    path('latest_product/', views.LatestProductList.as_view(), name='latest_product'),
    path('products/search/', views.search, name='search'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail')
]