from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/', CooperationRequestView.as_view()),
    path('delivery/', DeliveryView.as_view()),
]