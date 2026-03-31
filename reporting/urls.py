from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_form, name='report_form'),
    path('success/<str:ref>/', views.report_success, name='report_success'),
]
