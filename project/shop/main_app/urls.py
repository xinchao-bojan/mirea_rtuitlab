from django.urls import path
from .views import *
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', ShopListView.as_view()),
    path('shops/<int:shop_pk>/', ProductInShopView.as_view()),
    path('shops/<int:shop_pk>/<int:product_pk>/', ProductDetailView.as_view()),
    path('add_to_cart/<int:pk>/', AddToCartView.as_view()),
    path('delete_from_cart/<int:cp_pk>/', DeleteFromCartView.as_view()),
    path('clear_cart/', ClearCartView.as_view()),
    path('purchase/', PurchasingView.as_view()),
    path('cart_list/', CartListView.as_view()),
    path('delivery/', DeliveryOfProductsView.as_view()),
    path('moderate/<int:pk>/', ModerateProductView.as_view()),
    path('create_request/', CreateRequestView.as_view()),
]
urlpatterns += [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
]
