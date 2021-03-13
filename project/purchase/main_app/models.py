from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

CustomUser = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта', unique=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)
    default = models.BooleanField(verbose_name='Стандартная категория', default=False)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    date = models.DateTimeField(verbose_name='Дата покупки')
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Сумма, потраченная на товар')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    PAYMENT_METHODS = (
        ('noncash', 'безналичная оплата'),
        ('cash', 'оплата наличными'),
        ('thanks', 'за спасибо'),
        ('default', 'не указано'),
    )

    pm_choicer = models.CharField(max_length=7, verbose_name='Тип оплаты', default='default')

    def save(self, *args, **kwargs):
        if self.final_price <= 0:
            super().delete()
        else:
            self.date = timezone.now()
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.owner} {self.title}'


class PurchaseProduct(models.Model):
    title = models.CharField(max_length=127, verbose_name='Наименование')
    purchase = models.ForeignKey(Purchase, verbose_name='Покупка', on_delete=models.CASCADE)
    product_pk = models.PositiveIntegerField(verbose_name='Артикул продукта')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

    def __str__(self):
        return self.title
