from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

"""
class Profile:
    bio
    profile_image
    address
    user
"""

class Profile(models.Model):
    bio = models.TextField()
    profile_image=models.URLField(max_length=500)
    address = models.CharField(max_length=50)
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    def __str__(self) -> str:
        return f"<Profile for {self.user.username}>"




