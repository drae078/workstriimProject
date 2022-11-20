from django.shortcuts import render


# Create your views here.

def job_details(request, num=None):
    if request.method == "POST":

        print(request)
    job_number = num
    return render(request, 'job_details.html', context={'id': job_number})
