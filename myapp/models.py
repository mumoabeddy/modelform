from django.db import models


class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'student'
class Teacher(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return self.first_name
class Team(models.Model):
    team_name =models.CharField(max_length=30)
    team_points=models.CharField(max_length=10)
    team_position=models.CharField(max_length=10)
    def __str__(self):
        return self.team_name
class Post(models.Model):
    Title=models.CharField(max_length=30)
    Content=models.CharField(max_length=50)
    Author=models.CharField(max_length=30)
    Date=models.DateField()
    def __str__(self):
        return self.Title