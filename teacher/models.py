from django.db import models

# Create your models here.

from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)
    gradeYear = models.IntegerField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject, blank=True)