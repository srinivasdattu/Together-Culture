from django.urls import path
from tcapp import views

urlpatterns = [
    path('',views.hello, name='digitalconnection'),
    path('contenthub',views.contenthub,name='contenthub'),
    path('resources',views.resources,name='resources'),
]