from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #model-Database structure
    #views-Application Logic
    #Templet-Html User Interface
    #URL-coonects gthe browser requests to views
    

