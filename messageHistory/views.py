from django.shortcuts import render


# Create your views here.
def message_history(request, num=None):

    return render(request, 'messageHistory.html')

