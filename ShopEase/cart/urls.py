from django.urls import path
from .views import add_to_Cart,cart,checkout,hx_menu_cart,update_cart,hx_cart_total,success


urlpatterns = [
    path('', cart, name='my-cart'),
    path('success/', success, name='success'),
    path('cart-checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_Cart, name='add-to-cart'),
    path('update-cart/<int:product_id>/<str:action>/', update_cart, name='update-cart'),
    path('hx-menu-cart/', hx_menu_cart , name='hx-menu-cart'),
    path('hx-cart-total/', hx_cart_total, name='hx-cart-total')
]
