from django.shortcuts import render
from django.views import generic

from .models import *


class IndexView(generic.ListView):
	model = Product
	template_name = 'main/index.html'

	def get_queryset(self):
		return Product.objects.order_by('-published_date')[:5]
