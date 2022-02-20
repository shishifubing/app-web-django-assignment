# from django.shortcuts import render
# импортируем класс получения деталей объекта
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime as datetime_datetime


class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать
    # переменные в шаблон. В возвращаемом словаре context будут храниться все
    # переменные. Ключи этого словари и есть переменные, к которым мы сможем
    # потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавим переменную текущей даты time_now
        context['time_now'] = datetime_datetime.utcnow()
        # добавим ещё одну пустую переменную, чтобы на её примере посмотреть
        # работу другого фильтра
        context['value1'] = None
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'products/product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта
