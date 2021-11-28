from django.urls import path
from . import views

urlpatterns = [
    #Path del cores
    path('', views.services, name="services"),
]
