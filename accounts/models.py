from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio =models.TextField()
    avatar =models.URLField(max_length=500)

    def __str__(self) -> str:
        return f"<Profile for {self.user.username}>"

