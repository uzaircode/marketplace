from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
# from django.urls import reverse
# from django.views.generic import CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from store.forms import ProductForm
from store.models import Product


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_detail.html', {
        'user': user
    })


@login_required
def my_store(request):
    return render(request, 'userprofile/my_store.html')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'The product was added')

            return redirect('my_store')
    else:
        form = ProductForm()

    return render(request, 'userprofile/add_product.html', {
        'title': 'Add Product',
        'form': form,
    })


# class AddProduct(LoginRequiredMixin, CreateView):
#     model = Product
#     fields = ['category', 'title', 'description', 'price', 'image']
#     # form_class = ProductForm()
#     template_name = 'userprofile/add_product.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.slug = slugify(form.instance.title)
#         return super(AddProduct, self).form_valid(form)

#     def get_success_url(self):
#         return reverse('my_store')


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved')

            return redirect('my_store')
    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit Product',
        'form': form,
    })


@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = UserProfile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })
