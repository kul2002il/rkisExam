from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


class IndexView(generic.ListView):
	model = Product
	template_name = 'main/index.html'

	def get_queryset(self):
		return Product.objects.order_by('-published_date')[:5]


class ProductList(generic.ListView):
	model = Product


class ProductDetail(generic.DetailView):
	model = Product

	# def get(self, request, pk)

	def post(self, request, pk):
		message = []
		if 'user' in request:
			product = get_object_or_404(Product, pk=pk)
			number = int(request.POST['number'])
			Order(product=product, user=request.user, number=number).save()
			message.append('Заказ добавлен.')
		else:
			message.append('Необходимо войти в систему.')
		context = {'messages': message,}
		return self.get(self, request, pk)


def orderList(request):
	return render(request, 'main/userprofile_detail.html')


def loginView(request):
	message = []
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(username=data['username'], password=data['password'])
			if user:
				login(request, user)
				message.append('Успешное проникновение в систему.')
			else:
				message.append('Ошибка входа. Неверный логин или пароль.')
		else:
			message.append('Ошибка входа. Неверный формат данных.')
	else:
		form = LoginForm()
	context = {'form': form, 'messages': message}
	return render(request, 'main/login.html', context)


def logoutView(request):
	if request.user.is_authenticated:
		logout(request)
		message = 'Успешный выход из системы'
	else:
		message = 'Вход не был совершён.'
	context = {'messages': [message]}
	return render(request, 'main/logout.html', context)


def registerView(request):
	message = []
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			# fields = 'username', 'password', 'first_name', 'last_name', 'image', 'email'
			if UserProfile.objects.filter(username=data['username']):
				message.append('Данный логин занят.')
			else:
				user = UserProfile(username=data['username'],
				                   password=data['password'],
				                   first_name=data['first_name'],
				                   last_name=data['last_name'],
				                   image=data['image'],
				                   email=data['email'])
				user.save()
				login(request, user)
				redirect('some-view-name', foo='bar')
	else:
		form = UserProfileForm()
	context = {'form': form, 'messages': message}
	return render(request, 'main/register.html', context)
