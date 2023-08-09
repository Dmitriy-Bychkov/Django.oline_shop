from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product
from contacts.models import Contact


class ProductListView(ListView):
    """Контроллер для главной страницы со списком товаров"""

    model = Product
    extra_context = {
        'products': Product.objects.all()
    }


class ProductDetailView(DetailView):
    """Контроллер для страницы с описанием товара"""

    model = Product


# def contacts(request):
#     """Контроллер для страницы с контактной информацией"""
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя клиента: {name}\n'
#               f'Телефон: {phone}\n'
#               f'Сообщение: {message}')
#
#     contacts = Contact.objects.all()
#
#     return render(request, 'catalog/contact_detail.html', {'contacts': contacts})

# class ContactView(TemplateView):
#     template_name = 'catalog/contact_detail.html'
