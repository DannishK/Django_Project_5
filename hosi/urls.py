"""
URL configuration for medicine project.

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
from django.contrib import admin
from django.urls import path, include

from hosi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('query/',views.Querys, name='query'),
    path('Newsletter/', views.Newsletters, name='Newsletter'),
    path('appointmentslist/', views.Appointmentslist, name='appointmentslist'),
    path('editappointment/<int:id>/', views.editappointment, name='editappointment'),
    path('deleteappointment/<int:id>/', views.deleteappointment, name='deleteappointment'),
    path('querylist/', views.Querylist, name='querylist'),
    path('editquery/<int:id>/', views.editquery, name='editquery'),
    path('deletequery/<int:id>/', views.deletequery, name='deletequery'),
    path('newsletterlist/', views.Newsletterlist, name='newsletterlist'),
    path('editnewsletter/<int:id>/', views.editnewsletter, name='editnewsletter'),
    path('deletenewsletter/<int:id>/', views.deletenewsletter, name='deletenewsletter'),
]
