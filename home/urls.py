from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('qa/', views.qa, name='qa'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]