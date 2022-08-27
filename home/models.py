from django.db import models

# Create your models here.
class admission(models.Model):
    yname = models.CharField(max_length=122)
    pname = models.CharField(max_length=122)
    occupation = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    dob = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    email =  models.EmailField(max_length=122)
   
