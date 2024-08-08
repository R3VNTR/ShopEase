from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('browse/', views.browse, name='browse-items'),
    path('<slug:slug>/',views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/',views.product_details, name='product_detail'),
]
