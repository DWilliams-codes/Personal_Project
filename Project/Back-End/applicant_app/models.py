from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField()
    email = models.ForeignKey()