from django.shortcuts import render
from contacts.models import Contact


def contact_view(request):
    """Контроллер для страницы с контактной информацией"""

    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})
