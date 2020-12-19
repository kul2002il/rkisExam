from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('product/', ProductList.as_view(), name='products'),
	path('product/<int:pk>', ProductDetail.as_view(), name='productsDetail'),
	path('order/', orderList, name='order'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
