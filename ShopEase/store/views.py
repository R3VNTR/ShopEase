from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category,Review
from userprofile.models import UserProfile
from django.core.exceptions import ValidationError


star_ratings = range(1, 6)

def search(request):
    query = request.GET.get('q', '')
    product = Product.objects.filter(status = Product.ACTIVE).filter(Q(title__icontains=query) |
                                     Q(description__icontains=query) |
                                     Q(category__title__icontains=query))
    if request.user.is_authenticated:
        vendors = UserProfile.objects.filter(
            user__username__icontains=query).exclude(user=request.user)
    else:
        vendors = UserProfile.objects.filter(user__username__icontains=query)
    categories = Category.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'store/search.html', {'query': query, 'products': product, 'vendors': vendors, "categories": categories,'star_ratings': star_ratings})

def browse(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    vendors = UserProfile.objects.filter(is_seller=True)
    query1 = request.GET.get('search', '')
    query2 = request.GET.get('category', '')
    query3 = request.GET.get('vendor', '')
    if query1:
        products = products.filter(status = Product.ACTIVE).filter(Q(title__icontains=query1) |
                                     Q(description__icontains=query1))
    if query2 != 'all' and query2 != '':    
    
        products = products.filter(category__id = query2)

    if query3 != 'all' and query3 != '':    
     
        products = products.filter(user__id= query3)    

    return render(request,'store/browse_items.html' ,{'products':products,'categories':categories,'vendors':vendors,'star_ratings': star_ratings})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status = Product.ACTIVE)
  
    return render(request, 'store/category_detail.html', {"category": category, "products": products,'star_ratings': star_ratings})


def product_details(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status = Product.ACTIVE)

    if request.method == 'POST':
        try:
            rating = int(request.POST.get('rating', 4))
            if rating < 1 or rating > 5:
                raise ValidationError("Rating must be between 1 and 5")
        except ValueError:
            rating = 4 
        content = request.POST.get('content',).strip()

        if content:
            reviews = Review.objects.filter(created_by = request.user, product = product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()

            else:
                Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user,
                )

            return redirect('product_detail', category_slug=category_slug, slug=slug)


    return render(request, 'store/product_details.html', {"product": product,'star_ratings': star_ratings,})
