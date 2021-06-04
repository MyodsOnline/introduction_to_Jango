from django.utils import timezone
from django.shortcuts import render

from products.models import ProductCategory, Product

def index(request):
    context = {
        'title': 'GeekShop Main Page',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop Products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'date': timezone.now().date(),
    }
    return render(request, 'products/products.html', context)
