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

#  profile function

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
            return redirect('welcome')

    else:
        form = NewProfileForm()
    username=User.objects.all()    
    myProfile = Profile.objects.filter(username = current_user)
    projects = Projects.objects.filter(poster = current_user)    
    
    return render(request, 'profile.html', {"form": form, "username": username,"myProfile": myProfile, "projects":projects}) 

# edit profile function

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user

    if request.method =='POST':
        
        if Profile.objects.filter(username_id=current_user).exists():
            form = NewProfileForm(request.POST,request.FILES,instance=Profile.objects.get(username_id = current_user))    
        else:
            form=NewProfileForm(request.POST,request.FILES)   
           
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username=current_user
            profile.save()
            return redirect('profile', current_user.id)    
     
    else:
        if Profile.objects.filter(username_id = current_user).exists():
            form=NewProfileForm(instance =Profile.objects.get(username_id=current_user))
        else:
            form=NewProfileForm()     
            
    return render(request,'editProfile.html',{"form":form})                             
  
# rating function

@login_required(login_url='/accounts/login/')
def grade_rating(request,id):
     current_user=request.user
     project=Projects.objects.get(id=id)
     if request.method == 'POST':
        form = NewRatingForm(request.POST, request.FILES)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = current_user
            grade.project=project
            grade.total=int(form.cleaned_data['design'])+int(form.cleaned_data['content'])+int(form.cleaned_data['usability'])
            grade.avg= int(grade.total)/3
            grade.save()
        return redirect('welcome')
     else:
        form = NewRatingForm()
     return render(request, 'rating.html', {"form": form, 'project':project})  