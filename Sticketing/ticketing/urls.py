from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/home', views.clients, name = 'clients'),
    path('support/home', views.support, name='support'),
    path('director/home', views.director, name='director'),
]