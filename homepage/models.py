from django.db import models
from django.db import models

class Account_Details(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Emails = models.CharField(max_length = 30)
    Contac_no = models.IntegerField(12)
    Address = models.TextField()