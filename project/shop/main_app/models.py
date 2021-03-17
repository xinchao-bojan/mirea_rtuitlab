from decimal import Decimal

from django.contrib.auth import get_user_model
from django.utils import timezone

from django.db import models

CustomUser = get_user_model()


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    title = models.CharField(max_length=127, verbose_name='Наименование товара')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена', null=True)
    shop = models.ForeignKey('Shop', verbose_name='Магазин', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    moderated = models.BooleanField(verbose_name='Готов к продаже', default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.moderated:
            for elem in CartProduct.objects.filter(main_product=self):
                elem.delete()
        super().save(*args, **kwargs)


class Shop(models.Model):
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
    title = models.CharField(max_length=63, verbose_name='Название магазина', unique=True)
    address = models.CharField(max_length=127, verbose_name='Адрес')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    CATEGORY = (
        ('grocery', 'Продуктовый магазин'),
        ('restaurant', 'Ресторан'),
        ('clothes', 'Магазин одежды'),
        ('furniture', 'Магазин мебели'),
        ('electronics', 'Магазин электроники'),
    )

    category_choicer = models.CharField(choices=CATEGORY, verbose_name='Категория', max_length=15)

    def __str__(self):
        return self.title


class Cart(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    final_price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Общая стоимость', default=0)
    owner = models.OneToOneField(CustomUser, verbose_name='Владелец', on_delete=models.CASCADE)
    current_shop = models.CharField(max_length=127, verbose_name='Текущий магазин', default='')

    def save(self, *args, **kwargs):
        cp = self.cartproduct_set.all()
        self.final_price = 0
        for elem in cp:
            self.final_price += elem.price
        if self.final_price == 0:
            self.current_shop = ''
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Корзина пользователя {self.owner.email}'


class CartProduct(models.Model):
    class Meta:
        verbose_name = 'Продукт для корзины'
        verbose_name_plural = 'Продукты для корзины'
    main_product = models.ForeignKey(Product, verbose_name='Сам продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена', null=True)

    def save(self, *args, **kwargs):
        self.price = Decimal(self.main_product.price) * Decimal(self.quantity)
        super().save(*args, **kwargs)
        self.cart.save()

    def delete(self, *args, **kwargs):
        c = self.cart
        super().delete(*args, **kwargs)
        c.save()

    def __str__(self):
        return f'{self.main_product.title} (корзина)'


class ShopCheck(models.Model):
    class Meta:
        verbose_name = 'Чек для магазина'
        verbose_name_plural = 'Чеки для магазина'
    customer = models.ForeignKey(CustomUser, verbose_name='Покупатель', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата покупки')
    final_price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Сумма, потраченная на товар')

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        super().save(*args, **kwargs)


class CheckProduct(models.Model):
    class Meta:
        verbose_name = 'Продукт для чека'
        verbose_name_plural = 'Продукты для чека'
    title = models.CharField(max_length=127, verbose_name='Наименование')
    shop_check = models.ForeignKey(ShopCheck, verbose_name='Чек', on_delete=models.CASCADE)
    product_pk = models.IntegerField(verbose_name='Артикул продукта')
    quantity = models.IntegerField(verbose_name='Количество', default=0)
