# Generated by Django 3.1.7 on 2021-03-04 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('date', models.DateTimeField(verbose_name='Дата покупки')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Сумма, потраченная на товар')),
                ('pm_choicer', models.CharField(default='default', max_length=7, verbose_name='Тип оплаты')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category', verbose_name='Категория')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Наименование')),
                ('product_pk', models.IntegerField(verbose_name='Артикул продукта')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.purchase', verbose_name='Корзина')),
            ],
        ),
    ]
