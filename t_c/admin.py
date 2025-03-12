from django.contrib import admin
from .models import User, Event, Visit, DigitalContentModule, Suggestion, DigitalConnection, MemberDocument, Chat

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Visit)
admin.site.register(DigitalContentModule)
admin.site.register(Suggestion)
admin.site.register(DigitalConnection)
admin.site.register(MemberDocument)
admin.site.register(Chat)
