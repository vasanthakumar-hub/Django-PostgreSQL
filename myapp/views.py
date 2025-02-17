from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import is_valid_path

from . models import Product
from . forms import MyForm
# from myproject.myapp.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New Products are Coming Soon !')

def my_form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'myapp/my_form_template.html', {'form':form})

def success_view(request):
    return render(request, 'myapp/success_template.html')