from django.urls import path
from .views import *


urlpatterns = [
    path('request/', CooperationRequestView.as_view()),
    path('jopa/', KEK.as_view()),
]