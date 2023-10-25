from django.db import models

# Create your models here.


class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='Товар')
    description = models.CharField(max_length=200, verbose_name='Описание')
    price = models.FloatField(null=True, blank=False, verbose_name='Цена')
    creation_date = models.DateField(null=True, blank=False, verbose_name='Дата создания')
    update = models.DateField(null=True, blank=False, verbose_name='Дата обновления')
    owner = models.CharField(max_length=100, blank=True, verbose_name='Владелец')

    def __str__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, blank=False, verbose_name='Фамилия пользователя')
    email = models.EmailField(max_length=100, blank=True, verbose_name='Адрес электронной почты')
    password = models.CharField(max_length=100, blank=False, verbose_name='Пароль')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'