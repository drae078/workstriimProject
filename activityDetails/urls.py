from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_details),
    path('my_activity/', views.my_details, name='my_activity'),
]
