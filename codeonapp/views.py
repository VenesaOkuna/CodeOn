from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Projects, Profile, Rating, User
from .forms import NewProjectsForm, NewProfileForm,NewRatingForm



# Create your views here.
def welcome(request):
    projects = Projects.objects.all().order_by("post_date")
    profile = Profile.objects.all()

    return render(request, 'index.html' ,{'projects':projects}, {'profile':profile})

# search function
def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


#  function to add site

@login_required(login_url='/accounts/login/')
def add_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.poster = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectsForm()
    return render(request, 'create_site.html', {"form": form})
