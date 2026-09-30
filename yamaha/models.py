from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),#id=1
        ('moderator', 'Moderator'),#id=2
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    def __str__(self):
        return self.role
    
class Registration(models.Model):
    username = models.CharField(max_length=20, unique=True, default='default_user')
    email=models.EmailField(max_length=50, unique=True)
    password=models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.username
    
class Variants(models.Model):
    accessed_username=models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    id=models.AutoField(primary_key=True)
    model_name=models.CharField(max_length=30)
    manf_yr=models.DateField()
    colour=models.CharField(max_length=25)
    engine_type=models.CharField(max_length=10)
    Description=models.TextField(max_length=250)
    updated_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.model_name