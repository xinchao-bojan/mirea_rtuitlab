from django.db import models


class Factory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название завода', unique=True)
    productivity_coefficient = models.DecimalField(decimal_places=3, max_digits=5,
                                                   verbose_name='Коэффициент производительность')
    available = models.PositiveIntegerField(verbose_name='Свободный товар', null=True, blank=True)
    CATEGORY = (
        ('grocery', 'Продуктовый завод'),
        ('restaurant', 'Ресторанный завод'),
        ('clothes', 'Завод одежды'),
        ('furniture', 'Завод мебели'),
        ('electronics', 'Завод электроники'),
    )

    category_choicer = models.CharField(choices=CATEGORY, verbose_name='Категория', max_length=15)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        PRODUCTIVITY = {
            'grocery': 500,
            'restaurant': 500,
            'clothes': 200,
            'furniture': 50,
            'electronics': 25
        }
        self.available = PRODUCTIVITY[self.category_choicer] * self.productivity_coefficient
        for elem in self.deliveryrequest_set.all():
            self.available -= elem.quantity
        super().save(*args, **kwargs)


class ShopTitle(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название магазина', unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название продукта', unique=True)

    def __str__(self):
        return self.title


class DeliveryRequest(models.Model):
    shop = models.ForeignKey(ShopTitle, verbose_name='Магазин', on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, verbose_name='Завод', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    queue = models.PositiveIntegerField(verbose_name='Количество неотправленных поставок', default=1)

    def __str__(self):
        return f'{self.shop.title} + {self.factory.title}'

    def delete(self, *args, **kwargs):
        f = self.factory
        super().delete()
        f.save()
