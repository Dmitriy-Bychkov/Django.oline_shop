from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Контроллер для главной страницы со списком товаров"""

    model = Product
    extra_context = {
        'products': Product.objects.all()
    }


class ProductDetailView(DetailView):
    """Контроллер для страницы с описанием товара"""

    model = Product


class ProductCreateView(CreateView):
    """Контроллер для создания нового товара"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    """Контроллер для редактирования товара"""

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductDelete(DeleteView):
    """Контроллер для удаления продукта"""

    model = Product
    success_url = reverse_lazy('catalog:list')
