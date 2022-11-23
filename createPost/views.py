from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def new_post(request):
    return render(request, 'createPost.html')


def new_job(request):
    if request.method == "POST":
        messages.warning(request, message='Your post was added successfully!')
    return redirect('home')

