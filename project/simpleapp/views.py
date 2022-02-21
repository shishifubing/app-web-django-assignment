# from django.shortcuts import render
# импортируем класс получения деталей объекта
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime as datetime_datetime
from django.views import View
from django.core.paginator import Paginator
from .models import Product
from django.shortcuts import render


class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime_datetime.utcnow()
        context['value1'] = None
        return context


class Products(View):

    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get(self, request):
        products = Product.objects.order_by('-price')
        paginator = Paginator(products, 1)

        products = paginator.get_page(request.GET.get('page', 1))
        data = {'products': products}

        return render(request, 'sample_app/product_list.html', data)


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'products/product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта
