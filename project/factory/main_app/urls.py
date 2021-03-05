from django.urls import path
from .views import *


urlpatterns = [
    path('request/', CooperationRequestView.as_view()),
]