from django.utils import timezone
from django.shortcuts import render

def index(request):
    context = {
        'title': 'GeekShop Main Page',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop Products',
        'products': [
            {'name': 'худи черного цвета с монограммами adidas Originals', 'price': 6090.00, 'description': 'мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', 'img': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'синяя куртка The North Face', 'price': 23725.00, 'description': 'гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.', 'img': 'vendor/img/products/Blue-jacket-The-North-Face.png', 'in_basket': 'true'},
            {'name': 'коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00, 'description': 'материал с плюшевой текстурой. Удобный и мягкий.', 'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'черный рюкзак Nike Heritage', 'price': 2340.00, 'description': 'плотная ткань. Легкий материал.', 'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00, 'description': 'гладкий кожаный верх. Натуральный материал.', 'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00, 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.', 'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'},
        ],
        'btn_text_add': 'Отправить в корзину',
        'btn_text_rem': 'Удалить из корзины',
        'date': timezone.now().date(),
    }
    return render(request, 'products/products.html', context)
