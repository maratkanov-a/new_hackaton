# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=100)
    is_creator = models.BooleanField(default=False)
    enroll_id = models.CharField(max_length=500, default='')
    collection_id = models.CharField(max_length=500, default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.username


class Company(models.Model):
    geo = models.CharField(max_length=300)
    name = models.CharField(max_length=500)
    user = models.ForeignKey('User')

    def __unicode__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=500, default='')
    description = models.TextField(max_length=1000, default='')
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    geo = models.CharField(max_length=300)
    company = models.ForeignKey('Company')
    users = models.ManyToManyField(User, null=True, blank=True, default=None)
    img = models.ImageField()

    def __unicode__(self):
        return self.name
