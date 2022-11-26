from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.message_history, name='my_messages'),
]
