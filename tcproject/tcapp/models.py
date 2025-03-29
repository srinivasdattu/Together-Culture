from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('member', 'Community Member'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    interests = models.ManyToManyField('Interest', blank=True, related_name="users")  # Fix related name

    # Prevent clashes with Django's built-in auth.User model
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)
class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



    # Digital Content Modules
class DigitalContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    members = models.ManyToManyField(User, related_name='contenthub', blank=True)
    
# Digital Connections Board
class DigitalConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=[('need', 'Need'), ('offer', 'Offer')])
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)