from django.contrib import admin
from .models import User, DigitalContent, DigitalConnection


# Register your models here.
admin.site.register(User)
admin.site.register(DigitalContent)
admin.site.register(DigitalConnection)
