from django.shortcuts import render, redirect


# Create your views here.

def job_details(request, num=None):
    if request.method == "POST":
        print(request)
        print("Andrae")
    job_number = num
    images = ["image1", "image2"]
    return render(request, 'job_details.html', context={'id': job_number, 'images': images})


def claimed_job(request, job_id=None):
    if request.method == "POST":
        print("POST")
    else:
        print(request.method)
    job_id = 4
    return redirect(f'job_details', job_id)


def send_message(request, num=None):
    return render(request, 'sendMessage.html')
