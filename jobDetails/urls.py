from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_details, name='job_details')
]
