from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage , name = "project"),
    path('home/project/<str:pk>', views.product , name="product")
]