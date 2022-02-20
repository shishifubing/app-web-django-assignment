# from django.shortcuts import render
# импортируем класс получения деталей объекта
from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'products/product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта
