from django.urls import path
from .views import HomePage
from pages import views

urlpatterns = [
    path('', views.HomePage, name='home'),
]