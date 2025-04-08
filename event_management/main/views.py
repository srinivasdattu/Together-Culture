from django.shortcuts import render


def home(request):
    return render(request, 'home.html')



def admin_events_view(request):
    return render(request, 'admin_events.html')


def admin_create_event_view(request):
    return render(request, 'admin_create_event.html')



def member_events_view(request):
    return render(request, 'member_events.html')


def digital_content_view(request):
    return render(request, 'digital_content.html')
