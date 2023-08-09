from django.urls import path

from catalog.views import ProductDetailView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    #path('contacts/', ContactView.as_view()),
    #path('contacts/', views.contact_view, name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='view'),
]
