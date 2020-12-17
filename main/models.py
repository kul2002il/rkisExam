from django.db import models
from django.utils import timezone


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название')
	published_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)

	def __str__(self):
		return self.title
