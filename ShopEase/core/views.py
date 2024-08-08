from django.shortcuts import render
from store.models import Product,Category

def frontpage(request):
    star_ratings = range(1, 6)
    products = Product.objects.filter(status = Product.ACTIVE)[:6]
    categories = Category.objects.all()
    return render(request, 'core/frontpage.html', {"products":products, "categories":categories,'star_ratings': star_ratings})

def aboutpage(request):
    return render(request, 'core/about.html')
