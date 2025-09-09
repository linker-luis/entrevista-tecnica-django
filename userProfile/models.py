from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " " + self.lastName