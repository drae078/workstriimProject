from django.urls import path, include
from . import views

app_name: 'activityApp'
urlpatterns = [
    path('', views.profile, name='profile'),
]