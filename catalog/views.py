from django.views.generic import DetailView, ListView, TemplateView
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
