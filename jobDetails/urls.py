from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_details, name='job_details'),
    path('job_details/claimed_job/', views.claimed_job, name='claimed_job'),
]
