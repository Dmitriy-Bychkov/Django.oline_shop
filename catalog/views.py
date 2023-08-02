from django.shortcuts import render

from catalog.models import Product
from contacts.models import Contact


def index(request):
    """Контроллер для главной страницы"""
    latest_products = Product.objects.order_by('-creation_date')[:5].all()
    for product in latest_products:
        print(product.name)
    context = {'latest_products': latest_products}

    return render(request, 'catalog/index.html', context)


def contacts(request):
    """Контроллер для страницы с контактной информацией"""

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя клиента: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')

    contacts = Contact.objects.all()

    return render(request, 'catalog/contacts.html', {'contacts': contacts})
