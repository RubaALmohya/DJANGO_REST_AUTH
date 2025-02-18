from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NoteModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title