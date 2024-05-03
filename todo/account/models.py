from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __Str__(self):
        return self.username
    



    
