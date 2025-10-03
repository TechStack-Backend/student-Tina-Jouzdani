from django.db import models


class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    developers = models.ManyToManyField(Developer, related_name='projects', blank=True)



class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE,related_name="skills")
