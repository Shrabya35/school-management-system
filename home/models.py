from django.db import models

# Create your models here.
class admission1(models.Model):
    yname = models.CharField(max_length=122)
    pname = models.CharField(max_length=122)
    occupation = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    dob = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    email =  models.EmailField(max_length=122)


class payment1(models.Model):
    y2name = models.CharField(max_length=122)
    p2name = models.CharField(max_length=122)
    email2 = models.CharField(max_length=122)
    phone3 = models.CharField(max_length=122, blank=True, null=True)
    cardn = models.CharField(max_length=122)
    expm = models.CharField(max_length=122)
    pay = models.FloatField(max_length=122)

class admin1(models.Model):
    class_id = models.CharField(max_length=122)
    passw = models.CharField(max_length=122)
    time = models.CharField(max_length=122)
    grade = models.CharField(max_length=122)
    link = models.CharField(max_length=122)



    
    
   
