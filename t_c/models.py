from django.db import models

class User(models.Model):
    MEMBERSHIP_CHOICES = [
        ('community', 'Community Member'),
        ('key_access', 'Key Access Member'),
        ('creative_workspace', 'Creative Workspace Member'),
    ]

    INTERESTS_CHOICES = [
        ('caring', 'Caring'),
        ('sharing', 'Sharing'),
        ('creating', 'Creating'),
        ('experiencing', 'Experiencing'),
        ('working', 'Working'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES)
    predominant_interests = models.CharField(max_length=100, choices=INTERESTS_CHOICES)
    interests = models.CharField(max_length=100, blank=True)
    profile_status = models.CharField(max_length=50)
    joined_date = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.event_name

class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    activity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.full_name} - {self.activity}"

class DigitalContentModule(models.Model):
    module_name = models.CharField(max_length=100)
    module_description = models.TextField()
    module_date = models.DateField()

    def __str__(self):
        return self.module_name

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    based_on = models.CharField(max_length=100)

    def __str__(self):
        return f"Suggestion for {self.user.full_name}"

class DigitalConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    need_or_offer = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.need_or_offer} - {self.description}"

class MemberDocument(models.Model):
    document_name = models.CharField(max_length=100)
    document_content = models.TextField()

    def __str__(self):
        return self.document_name

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.full_name}"
