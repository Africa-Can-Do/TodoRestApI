from django.db import models

# Create your models here.



class Todo(models.Model):
    title= models.CharField(blank=False, max_length=50)
    description = models.CharField(max_length=100)
    created= models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) :
        return self.title
    

