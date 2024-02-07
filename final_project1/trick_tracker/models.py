from django.db import models
from django.contrib.auth.models import User

class Trick(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trick = models.ForeignKey(Trick, on_delete=models.CASCADE)
    selection = models.CharField(max_length=20, choices=[
        ('not_landed', 'Not Landed'),
        ('landed_sketchy', 'Landed Sketchy'),
        ('landed_clean', 'Landed Clean'),
        ('on_lock', 'On Lock'),
    ])
