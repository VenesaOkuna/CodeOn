from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Projects, Profile, Rating, User


# Create your views here.
def welcome(request):
    projects = Projects.objects.all().order_by("post_date")
    profile = Profile.objects.all()

    return render(request, 'index.html' ,{'projects':projects}, {'profile':profile})


