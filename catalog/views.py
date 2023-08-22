from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Контроллер для главной страницы со списком товаров"""

    model = Product

    def get_context_data(self, **kwargs):
        """Выводим в общий список информацию об активных версиях продукта"""

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current_version=True).first()
            if active_version:
                product.active_version_number = active_version.version_number
                product.active_version_name = active_version.version_name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


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
