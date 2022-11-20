from django.shortcuts import render


# Create your views here.
def my_details(request):
    return render(request, 'my_details.html')
