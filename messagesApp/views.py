from django.shortcuts import render


# Create your views here.
def my_messages(request):
    return render(request, 'my_messages.html')
