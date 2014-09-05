from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
    def __str__(self):
        
        return self.user.username

class post(models.Model):
    poster = models.CharField(max_length=25)
    submission = models.CharField(max_length=255)

    def __str__(self):
        return str(self.poster + ": " + self.submission)
        
    
