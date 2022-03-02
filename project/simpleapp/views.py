from django.views.generic import ListView, DetailView
from .filters import ProductFilter
from .models import Product
from django.views import View
from django.core.paginator import Paginator
from .models import Product
from django.shortcuts import render


class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(
            self.request.GET,
            queryset=self.get_queryset())
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

        return render(request, 'products/products.html', data)


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'
