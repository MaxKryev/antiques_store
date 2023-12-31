# Generated by Django 4.2.5 on 2023-10-25 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='Имя пользователя')),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Фамилия пользователя')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Адрес электронной почты')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Товар')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.owner')),
            ],
        ),
    ]
