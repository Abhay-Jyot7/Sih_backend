from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_predict.as_view()),
]