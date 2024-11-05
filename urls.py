"""
URL configuration for client_project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# client_project_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

# Define a simple view for the root URL
def root_view(request):
    # Option 1: Return a welcome message
    return HttpResponse("Welcome to the Client Project Management API")

    # Option 2: Redirect to /api/
    # return redirect('/api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Assuming 'clients' app has its URLs defined in clients/urls.py
    path('', root_view),  # Map the root URL to root_view
]

