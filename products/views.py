from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop Main Page',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop Products',
        'categories': ProductCategory.objects.all(),
        'date': timezone.now().date(),
    }
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    # if category_id:
    #     context['products'] = Product.objects.filter(category_id=category_id)
    # else:
    #     context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
