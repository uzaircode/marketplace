from django.views.generic.list import ListView
from django.shortcuts import render
from store.models import Product


# def frontpage(request):
#     products = Product.objects.all()[0:6]
#     return render(request, 'core/frontpage.html', {
#         'products': products
#     })

class frontpage(ListView):
    """ Display all products """
    model = Product


def about(request):
    return render(request, 'core/about.html')
