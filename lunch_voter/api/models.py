from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    build_version = models.CharField(max_length=20)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.DateField()
    items = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'menu')  # 1 голос за день
