from django.urls import path

from contacts.views import ContactDetailView
from contacts.apps import ContactsConfig
app_name = ContactsConfig.name

urlpatterns = [
    path('<int:pk>', ContactDetailView.as_view()),
    #path('contacts/', views.contact_view, name='contacts'),
    #path('products/<int:pk>/', ProductDetailView.as_view(), name='view'),
]