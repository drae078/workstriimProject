from django.shortcuts import render, redirect


# Create your views here.

def job_details(request, num=None):
    if request.method == "POST":

        print(request)
        print("Andrae")
    job_number = num
    return render(request, 'job_details.html', context={'id': job_number})


def claimed_job(request, job_id=None):
    if request.method == "POST":
        print("POST")
    else:
        print(request.method)
    job_id = 4
    return redirect(f'job_details', job_id)
