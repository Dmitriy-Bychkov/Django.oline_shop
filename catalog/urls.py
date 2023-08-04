from django.urls import path

from catalog.views import index, contacts, home
from contacts import views

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('contacts/', views.contact_view, name='contacts'),
    path('products/<int:product_id>/', home),
]
