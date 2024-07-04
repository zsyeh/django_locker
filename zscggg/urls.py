"""
URL configuration for zscggg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from myapp import views as myapp
from myapp.views import create_user_device

urlpatterns = [
    path('create/', create_user_device, name='create_user_device'),
    # path('success/', success_url, name='success_url'),
    path('', myapp.index, name='index'),
    path('dashboard/', myapp.dashboard, name='dashboard'),
    path('live/', myapp.live, name='live'),
    path('user_device_form/', myapp.user_device_form, name='user_device_list'),
    path('user_device_list/', myapp.user_device_list, name='user_device_list'),
    path('user_device_detail/', myapp.user_device_detail, name='user_device_detail'),
    path('user_device_edit/', myapp.user_device_edit, name='user_device_edit'),
    path('user_device_delete/', myapp.user_device_delete, name='user_device_delete'),
    path('user_device_create/', myapp.user_device_create, name='user_device_create'),
    path('user_device_update/', myapp.user_device_update, name='user_device_update'),
    path('search_form/', myapp.search_form, name='search_form'),
    path('search/', myapp.search, name='search'),
    path('search-post/', myapp.search_post, name='search_post'),
    path('user_view/', myapp.user_view, name='user_view'),
    path('success_url/', myapp.success_url, name='success_url'),
    path('delete/<str:name>/', myapp.delete_user, name='delete_user'),
    path('index1/', myapp.index1, name='index1'),
    
    path('status/', myapp.status, name='status'),
]