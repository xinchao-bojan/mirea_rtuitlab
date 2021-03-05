from django.contrib import admin

from .models import *

admin.site.register(Factory)
admin.site.register(ShopTitle)
admin.site.register(Product)
admin.site.register(DeliveryRequest)