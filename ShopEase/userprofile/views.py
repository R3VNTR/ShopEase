from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import CustomAuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from store.forms import ProductForm
from store.models import Product, Review
from order.models import Order,OrderItem
from .forms import UserProfileForm
from django.utils import timezone

star_ratings = range(1, 6)
def vendor_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    products = user.products.filter(status=Product.ACTIVE)

    highest_review = None

    if products.exists():
        highest_review = Review.objects.filter(product__in=products).order_by('-rating', '-created_at').first()


    return render(request, 'userprofile/vendor_details.html', {"userx": user, 'products': products,'star_ratings': star_ratings,'highest_review': highest_review, })


# @login_required
# def my_store(request):
#     products = request.user.products.exclude(status=Product.DELETED)
#     deleted_products = request.user.products.filter(status=Product.DELETED)
#     return render(request, 'userprofile/my_store.html', {'products': products,'deleted_products':deleted_products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, "The product was added!")
            return redirect('myaccount')
    else:
        form = ProductForm()

    return render(request, 'userprofile/product_form.html', {'form': form, 'title': 'Add Product'})


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "The product was updated!")
            return redirect('myaccount')

    else:
        form = ProductForm(instance=product)
    return render(request, 'userprofile/product_form.html', {'form': form, 'title': 'Edit Product', 'product': product})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    product.status = Product.DELETED
    product.save()
    messages.success(request, "The product was deleted!")
    return redirect('myaccount')

@login_required
def undo_product_status(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    product.status = Product.ACTIVE
    product.save()
    messages.success(request, "The product status was updated!")
    return redirect('myaccount')


@login_required
def my_account(request):
    products = request.user.products.filter(status=Product.ACTIVE)
    deleted_products = request.user.products.filter(status=Product.DELETED)

    
    # pending_orders = Order.objects.filter(
    # items__product__user=request.user, 
    # status=Order.ORDERED 
    # ).distinct()

    pending_orders = OrderItem.objects.filter(
    product__user=request.user
    ).order_by('-id').distinct()


    highest_review = None

    if products.exists():
        highest_review = Review.objects.filter(product__in=products).order_by('-rating', '-created_at').first()


    return render(request, "userprofile/myaccount.html", {'products': products,'deleted_products':deleted_products,'star_ratings': star_ratings,'highest_review': highest_review, 'pending_orders':pending_orders})


@login_required
def order_details(request,oid,otm):
    order = get_object_or_404(Order, id=oid)
    order_item = get_object_or_404(OrderItem, id=otm)
    return render(request, 'userprofile/order_details.html',  {'order': order,'order_item':order_item})


@login_required
def approve_order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if order_item.status == OrderItem.ORDERED:
        order_item.status = OrderItem.SHIPPED
        order_item.shiped_date = timezone.now()
        order_item.save()
    return redirect('myaccount')

@login_required
def reject_order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    if order_item.status == OrderItem.ORDERED:
        order_item.status = OrderItem.REJECTED
        order_item.shiped_date = timezone.now()
        order_item.save()
    return redirect('myaccount')



@login_required
def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save() 

            form.save()  
            messages.success(request, "Your profile was updated!")
            return redirect('myaccount')  
    else:
        form = UserProfileForm(instance=user_profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })

    return render(request, 'userprofile/update_user_profile.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            userpofile = UserProfile.objects.create(user=user)

            return redirect('frontpage')

    else:
        form = CustomUserCreationForm()

    return render(request, 'userprofile/signup.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('frontpage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'userprofile/login.html', {'form': form})
