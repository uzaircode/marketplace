# from django.views.generic.list import ListView
from django.shortcuts import render
from store.models import Product


def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    return render(request, 'core/frontpage.html', {
        'products': products
    })


# class frontpage(ListView):
#     """ Display all products """
#     model = Product
#     template_name = 'frontpage.html'
#     context_object_name = 'products'


def about(request):
    return render(request, 'core/about.html')
