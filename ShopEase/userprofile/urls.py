from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('item-ordered/<int:oid>/<int:otm>/', views.order_details, name="item-ordered"),
    path('order-item/approve/<int:pk>/', views.approve_order_item, name='approve-order-item'),
    path('order-item/reject/<int:pk>/', views.reject_order_item, name='reject-order-item'),
    path('myaccount/', views.my_account, name="myaccount"),
    path('myaccount/update', views.update_profile, name="update_my_profile"),
    # path('my-store/', views.my_store, name="my-store"),
    path('my-store/add-product/', views.add_product, name="add-product"),
    path('my-store/edit-product/<int:pk>/', views.edit_product, name='edit-product'),
    path('my-store/delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    path('my-store/recover-product-status/<int:pk>/', views.undo_product_status, name='recover-product'),
    path('vendors/<int:pk>/', views.vendor_detail, name="vendor-details")
]
