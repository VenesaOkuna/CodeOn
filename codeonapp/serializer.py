from rest_framework import serializers
from .models import Projects, Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'description')
        
class ProfileSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'email', 'phone_number')        