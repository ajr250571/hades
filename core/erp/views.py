from django.shortcuts import render

from core.erp.models import Product, Category


def myfirstview(request):
    data = {
        'name': 'Armandor',
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', data)


def mysecondview(request):
    data = {
        'name': 'Armandor',
        'products': Product.objects.all()
    }

    return render(request, 'second.html', data)
