from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)

class Audit(models.Model):
    message = models.CharField(max_length=255)