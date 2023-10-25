from django.db import models
import uuid

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.FloatField(null=True, blank=False, verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Owner(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия пользователя')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Адрес электронной почты')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
