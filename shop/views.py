from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product = Products.objects.all()

    item_name=request.GET.get('item_name')

    if item_name != '' and item_name is not None:
        product = product.filter(title__icontains = item_name)

    paginator = Paginator(product, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'shop/index.html',{'products':products})

def details(request,id):
    product = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})

def checkout(request):
    return render(request, 'shop/checkout.html')

