from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Entry(models.Model):
    title = models.CharField(max_length=255)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    modified_at = models.DateTimeField(auto_now=True,editable=False)


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural="Entries"