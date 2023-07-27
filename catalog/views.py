from django.shortcuts import render


def index(request):
    """Контроллер для главной страницы"""

    return render(request, 'catalog/index.html')


def contacts(request):
    """Контроллер для страницы с контактной информацией"""

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя клиента: {name}\n'
              f'Телефон: {phone}\n'
              f'Сообщение: {message}')

    return render(request, 'catalog/contacts.html')
