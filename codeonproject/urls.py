"""codeonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from . import settings

from codeonapp.forms import NewProfileForm


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Other URL patterns ...
    path('accounts/profile/', RegistrationView.as_view(success_url='/', form_class=NewProfileForm), name='profile'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Code on app
    path('', include('codeonapp.urls')),
    #tinymce
    path('tinymce/', include('tinymce.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
