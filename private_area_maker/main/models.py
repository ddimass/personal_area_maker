from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Header(models.Model):
    fast_actions = (
        (0, 'No actions'),
        (1, 'Messages'),
        (2, 'Messages, User'),
        (3, 'Messages, User, State')
    )
    types = (
        (0, 'Full line'),
        (1, 'Inline'),
    )
    name = models.CharField(max_length=100)
    logo_path = models.FileField(upload_to='uploads/', null=True, default=None, blank=True)
    logo_text = models.CharField(max_length=100, null=True, default=None, blank=True)
    fast_action = models.IntegerField(choices=fast_actions, default=0)
    type = models.IntegerField(choices=types, default=0)
    project = models.OneToOneField(Project, on_delete=models.SET_DEFAULT, null=True, default=None, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Menu_item(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='uploads/', null=True,  default=None, blank=True)
    text = models.CharField(max_length=50, null=True,  default=None, blank=True)
    action = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    h1 = models.CharField(max_length=100, null=True, default=None)
    items = models.ManyToManyField(Menu_item, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Sidebar(models.Model):
    types = (
        (0, 'Enable sidebar'),
        (1, 'Disable sidebar'),
    )
    name = models.CharField(max_length=100)
    logo_path = models.FileField(upload_to='uploads/', null=True, default=None, blank=True)
    logo_text = models.CharField(max_length=100, null=True, default=None, blank=True)
    type = models.IntegerField(choices=types, default=0)
    menus = models.ManyToManyField(Menu, blank=True)
    project = models.OneToOneField(Project, on_delete=models.SET_DEFAULT, null=True, default=None, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




