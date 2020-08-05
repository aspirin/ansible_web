from django.db import models

# Create your models here.

class Projects(models.Model):
    projectname = models.CharField(max_length=50)
    path = models.CharField(max_length=100)
    class Meta:
        db_table = 'deploy_projects'

class Mycommand(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, )
    cmd = models.CharField(max_length=200)
    logpath = models.CharField(max_length=100)
    class Meta:
        db_table = 'deploy_mycommand'