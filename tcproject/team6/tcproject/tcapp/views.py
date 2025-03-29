from django.shortcuts import render,HttpResponse
from .models import DigitalContent
# Create your views here.
def hello(request):
    return render(request,'digitalconnection.html')
def contenthub(request):
    return render(request,'contenthub.html')
def resources(request):
    return render(request,'resources.html')
def content_list(request):
    digital_content_list = DigitalContent.objects.all()
    return render(request, 'content_list.html', {'digital_content_list': digital_content_list})