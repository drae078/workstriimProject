from django.shortcuts import render
from django.http import HttpResponse
from activityDetails.views import my_details


# Create your views here.
def profile(request):
    return render(request, 'profile.html')

