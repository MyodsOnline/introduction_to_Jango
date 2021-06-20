from django.utils import timezone
from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop Main Page',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'GeekShop Products',
        'categories': ProductCategory.objects.all(),
        'date': timezone.now().date(),
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
