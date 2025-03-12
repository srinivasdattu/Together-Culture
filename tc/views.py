from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request,'homepage(team6).html')
def admin1(request):
    return render(request,"admin.html")
def member(request):
    return render(request,"member.html")
def contenthub(request):
    return render(request,"contenthub.html")
def resources(request):
    return render(request,"resources.html")
def digitalconnections(request):
    return render(request,"digitalconnections.html")
def event(request):
    return render(request,"event.html")
def insights(request):
    return render(request,"insights.html")
def membership(request):
    return render(request,"membership.html")
def adminlogin(request):
    return render(request, "adminlogin.html")
def memberlogin(request):
    return render(request, "memberlogin.html")
def signup(request):
    return render(request,"signup.html")
def settings(request):
    return render(request, "settings.html")