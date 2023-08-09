from django.shortcuts import render
from django.views.generic import DetailView

from contacts.models import Contact


# def contact_view(request):
#     """Контроллер для страницы с контактной информацией"""
#
#     contacts = Contact.objects.all()
#     return render(request, 'contact_detail.html', {'contacts': contacts})

class ContactDetailView(DetailView):
    model = Contact
