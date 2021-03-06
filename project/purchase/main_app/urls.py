from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('create_purchase/', CreatePurchaseView.as_view()),
    path('purchase_list/', PurchaseListView.as_view()),
    path('purchase_by_category/<str:category>/', PurchaseByCategoryListView.as_view()),
    path('update_purchase/', UpdatePurchaseView.as_view()),
    path('create_category/', CreateCategoryView.as_view()),
    path('check_user/', CheckAuthorization.as_view()),
    path('admin/', admin.site.urls)

]

urlpatterns += [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
]
