from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('image')
    bio = models.CharField(max_length =60)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    username = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile',null=True)
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()    
        
    def update_profile(self):
        self.update()

    def delete_profile(self):
        self.delete()

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/default-profile.jpg"


class Projects (models.Model):
    title = models.CharField(max_length =40)
    image = CloudinaryField('image')
    description =  HTMLField()
    profile = models.ForeignKey(Profile,null = True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE , null=True) 
    post_date=models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length =200)
    
    def __str__(self):
        return self.title
    
    def save_projects(self):
        self.save()
        
    def update_projects(self):
        self.update()

    def delete_projects(self):
        self.delete() 
                
    @classmethod
    def search_by_title(cls,search_term):
        titles = cls.objects.filter(title__icontains=search_term)
        return titles  
    