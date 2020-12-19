from django.contrib import admin

from.models import *


# Товары и их фото
class PhotoProductInline(admin.TabularInline):
	model = PhotoProduct
	extra = 3


class ProductAdmin(admin.ModelAdmin):
	inlines = [PhotoProductInline]


admin.site.register(Product, ProductAdmin)


# Пользователь и его заказы
class OrderInline(admin.TabularInline):
	model = Order


class UserProfileAdmin(admin.ModelAdmin):
	inlines = [OrderInline]


admin.site.register(UserProfile, UserProfileAdmin)
