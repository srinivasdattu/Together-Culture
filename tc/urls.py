"""
URL configuration for tc project.

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
from django.urls import path
from t_c.views import hello,member,contenthub,resources,digitalconnections,membership,insights,event,admin1,adminlogin,memberlogin,settings,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",hello,name="home.html"),
    path("admin.html/",admin1,name='admin'),
    path("member.html/",member,name='member'),
    path("contenthub.html/",contenthub,name='content'),
    path("resources.html/",resources,name='resources'),
    path("digitalconnections.html/",digitalconnections,name='digitalconnections'),
    path("membership.html/",membership,name='membership'),
    path("insights.html/",insights,name='insights'),
    path("event.html/",event,name='event'),
    path("adminlogin.html/",adminlogin,name='adminlogin'),
    path("memberlogin.html/",memberlogin,name='memberlogin'),
    path("settings.html/",settings,name='settings'),
    path("signup.html/",signup,name="signup"),
    path("memberlogin.html/member.html/",member,name='member'),
    path("memberlogin.html/member.html/member.html",member,name='member'),
    path("memberlogin.html/member.html/event.html",event,name='event'),
    path("memberlogin.html/member.html/digitalconnections.html",digitalconnections,name='digitalconnections'),
    path("memberlogin.html/member.html/settings.html",settings,name='settings'),
    path("memberlogin.html/member.html/homepage(team6).html",hello,name='home'),
]
