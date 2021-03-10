from django.db import models

# Create your models here.

class Destination(models.Model):

    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    massage= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Demo(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
