from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

WEEKDAY_CHOICES = [
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
]


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Routine(models.Model):
    user = models.ForeignKey(User, related_name='routines', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, related_name='routines')
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAY_CHOICES)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} ({self.user})"
    


