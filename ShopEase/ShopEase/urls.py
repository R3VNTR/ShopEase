from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from core.views import frontpage,aboutpage
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('inbox/',include('coversation.urls')),
    path('user/',include('userprofile.urls')),
    path('store/',include('store.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
