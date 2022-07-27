from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('form/', views.formView, name='form'),
    path('out/', views.logoutView, name='out'),
    ]

