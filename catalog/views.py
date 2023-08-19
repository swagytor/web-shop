from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def home(request):
    context = {'object_list': Product.objects.all(),
               'title': 'SkyStore Главная'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {'title': 'SkyStore Контакты'}
    return render(request, 'catalog/contacts.html', context)


def product_details(request, pk):
    object_items = Product.objects.get(pk=pk)
    context = {'object': Product.objects.filter(id=pk)[0],
               'title': f"{object_items.product_name}"}

    return render(request, 'catalog/product.html', context)
