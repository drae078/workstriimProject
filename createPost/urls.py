from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_post, name='new_post'),
    path('new_job', views.new_job, name='new_job')
]
