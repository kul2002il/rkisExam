from django.contrib import admin

from.models import *


admin.site.register(UserProfile)


class PhotoProductInline(admin.TabularInline):
	model = PhotoProduct
	extra = 3


class ProductAdmin(admin.ModelAdmin):
	inlines = [PhotoProductInline]


admin.site.register(Product, ProductAdmin)
