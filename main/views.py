from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import *


class IndexView(generic.ListView):
	model = Product
	template_name = 'main/index.html'

	def get_queryset(self):
		return Product.objects.order_by('-published_date')[:5]


class ProductList(generic.ListView):
	model = Product


class ProductDetail(generic.DetailView):
	model = Product

	def post(self, request, pk):
		product = get_object_or_404(Product, pk=pk)
		number = int(request.POST['number'])
		Order(product=product, user=request.user, number=number).save()
		return self.get(self, request)


def orderList(request):
	return render(request, 'main/userprofile_detail.html')
