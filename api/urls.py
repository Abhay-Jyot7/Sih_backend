from django.urls import path
from . import views

urlpatterns = [
    path('crop/', views.crop_predict.as_view()),
    path('fertilizer/', views.fertilizer_predict.as_view()),
]