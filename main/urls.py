from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('news/', ProductList.as_view(), name='news'),
	path('news/<int:pk>/', ProductDetail.as_view(), name='newsDetail'),
	path('repair/', orderList, name='repair'),
	path('login/', loginView, name='login'),
	path('logout/', logoutView, name='logout'),
	path('register/', registerView, name='register'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
