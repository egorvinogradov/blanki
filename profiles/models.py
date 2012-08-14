#coding:utf-8
from django.db import models


class Profile(models.Model):

    user = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
