from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, ProductDelete, \
    CategoryProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
    path('category/<int:category_pk>', CategoryProductListView.as_view(), name='product_category'),
]
