from django.db import models

# Create your models here.

class step_count(models.Model):
    time = models.DateTimeField()
    Count = models.FloatField()
    def __str__(self):
        return f'{self.time} - {self.Count}'

class calories_burnt(models.Model):
    time = models.DateTimeField()
    Joule = models.FloatField()
    def __str__(self):
        return f'{self.time} - {self.Joule}'

class distance_covered(models.Model):
    time = models.DateTimeField()
    KM = models.FloatField()
    def __str__(self):
        return f'{self.time} - {self.KM}'

class heart_rate(models.Model):
    time = models.DateTimeField()
    BPM = models.FloatField()
    def __str__(self):
        return f'{self.time} - {self.BPM}'


