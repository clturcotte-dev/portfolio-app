from django.db import models

#class Test(models.Model):
#    firstName = models.CharField(max_length=25)
#    lastName = models.CharField(max_length=25)

class Project(models.Model):
    projectName = models.CharField(max_length=100)
    projectDescription = models.CharField(max_length=500)
    projectDate = models.DateField(auto_now=True)