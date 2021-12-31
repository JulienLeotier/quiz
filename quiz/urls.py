"""quiz URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from chat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('categories/<str:room_name>/', views.roomCategories, name='room'),
    path('categories/admin/<str:room_name>/',
         views.adminCatagorie, name='room'),
    path('onlyQuestion/<str:room_name>/', views.onlyQuestion, name='question'),
    path('room/admin/<str:room_name>/', views.admin, name='admin'),
    path('root/', views.ref, name='ref'),
    path('root/admin/', views.refadmin, name='ref'),
    path('tab/', views.tab, name='tab'),
    path('room/admin/display/<str:room_name>/', views.display, name='display'),
]
