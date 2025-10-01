from django.db import models

class Test(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)