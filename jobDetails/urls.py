from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_details, name='job_details'),
    path('/send_message/', views.send_message, name='send_message'),
    path('job_details/claimed_job/', views.claimed_job, name='claimed_job'),
]
