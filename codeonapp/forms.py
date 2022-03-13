from django import forms
from .models import Merch, Projects,Profile,Rating

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['profile', 'post_date', 'poster', 'description']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']        
       
class NewRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['profile','project','user','total','avg']  

class NewMerchForm(forms.ModelForm):
    class Meta:
        model = Merch
               