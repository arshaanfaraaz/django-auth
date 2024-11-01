from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user