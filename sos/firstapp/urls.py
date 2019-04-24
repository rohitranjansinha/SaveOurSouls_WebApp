"""sos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from django.conf import *

from firstapp.views import *

app_name = 'firstapp'

urlpatterns = [
    path('',home_view,name="home"),
    path('register_user/',register_user),
    path('login_user/', login_user, name="user"),
    path('login_hospital/', login_hospital, name="hospital"),
    path('about/', about_view),
    path('contact/', contact_view),
    path('faq/', faq_view),
    path('register_hospital/', register_hospital),
    path('profile/', ward_hospital),
    path('opd/', opd_hospital),
    path('update/', update_hospital),
    path('hospital_location/', hospital_location),
    path('logout/', logout),
    path('submit/', main_view),
]
