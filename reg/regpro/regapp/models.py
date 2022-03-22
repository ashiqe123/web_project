from django.db import models

# Create your models here.
class spec(models.Model):
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    head=models.CharField(max_length=10)