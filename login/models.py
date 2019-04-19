from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmPassword = models.CharField(max_length=200)

