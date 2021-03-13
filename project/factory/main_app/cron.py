import json

import requests
from decouple import config

from main_app.models import ShopTitle, DeliveryRequest

print("00000000000000000000000000000000000000000000")
for s in ShopTitle.objects.all():
    queryset = []
    for dr in DeliveryRequest.objects.filter(shop=s):
        d = {'title': dr.product.title,
             'quantity': dr.quantity}
        queryset.append(d)

    data = {'key': config('SHOP_SECRET_KEY'),
            'shop': s.title,
            'products': json.dumps(queryset)}
    try:
        r = requests.post('http://localhost:80/api/shop/delivery/',
                          data=data)
        for dr in DeliveryRequest.objects.filter(shop=s):
            dr.queue = 1
            dr.save()
    except OSError:
        for dr in DeliveryRequest.objects.filter(shop=s):
            dr.queue += 1
            dr.save()
