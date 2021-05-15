from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
	image = models.ImageField(verbose_name="Аватарка", null=True)


class Product(models.Model): # Новость
	title = models.CharField(max_length=255, verbose_name='Название')
	description = models.TextField(verbose_name='Описание товара', default='')
	published_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)

	def __str__(self):
		return self.title


class PhotoProduct(models.Model): # Фото новости
	image = models.ImageField(verbose_name="Фото товара")
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.image.__str__()


class Order(models.Model): # Лайки
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	number = models.IntegerField(verbose_name="Количество")

	def __str__(self):
		return self.product.__str__()
