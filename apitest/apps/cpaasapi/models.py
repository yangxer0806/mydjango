from django.db import models

# Create your models here.

class PaaS(models.Model):
    called = models.CharField(max_length=100)
    calledDisplay = models.CharField(max_length=100)
    templateID = models.CharField(max_length=100)
    params = models.CharField(max_length=500)
    playTimes = models.IntegerField()
    playDelay = models.IntegerField()
    data = models.TextField()