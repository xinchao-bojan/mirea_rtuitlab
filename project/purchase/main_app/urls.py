from django.urls import path
from .views import *

urlpatterns = [
    path('create_purchase/', CreatePurchaseView.as_view()),
    path('purchase_list/', PurchaseListView.as_view()),
    path('update_purchase/<int:pk>/', UpdatePurchaseView.as_view()),
    path('create_category/', CreateCategoryView.as_view()),
]
