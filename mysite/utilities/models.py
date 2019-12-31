from django.db import models

class Job(models.Model):
    endpoint = models.CharField(max_length=20)
    parameters = models.CharField(max_length=300)
    startTime = models.DateField()





# Create your models here.
