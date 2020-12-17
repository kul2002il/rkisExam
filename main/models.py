from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название')
	published_date = models.DateTimeField(verbose_name='Дата публикации')
