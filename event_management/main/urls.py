from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_events/', views.admin_events_view, name='admin_events'),
    path('admin_create_event/', views.admin_create_event_view, name='admin_create_event'),
    path('member_events/', views.member_events_view, name='member_events'),
    path('digital_events/', views.digital_content_view, name='digital_events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
