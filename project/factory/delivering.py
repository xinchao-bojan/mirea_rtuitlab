from .main_app.models import *

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
        r = requests.post('http://localhost:8002/api/shop/delivery/',
                          data=data)
        for dr in DeliveryRequest.objects.filter(shop=s):
            dr.queue = 1
            dr.save()
    except OSError:
        for dr in DeliveryRequest.objects.filter(shop=s):
            dr.queue += 1
            dr.save()
