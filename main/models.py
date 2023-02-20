from django.db import models

# Create your models here.

class Student(models.Model):
    GENDERS = (
        ('male', 'male'),
        ('female', 'female'),
    )
    DIRECTIONS = (
        ('Back-end', 'Back-end'),
        ('Front-end', 'Front-end'),
        ('UX/UI', 'UX/UI'),
        ('Fullstack', 'Fullstack'),
    )
    full_name = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, choices=DIRECTIONS)
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices=GENDERS)
