# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

class DefaultStack(models.Model):
    infrastructure_name = models.CharField(max_length=20)
    infrastructure_owner = models.ForeignKey(User,default=None)
    infrastructure_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.infrastructure_name

class CustomStack(models.Model):
    infrastructure_name = models.CharField(max_length=20)
    infrastructure_owner = models.ForeignKey(User,default=None)
    infrastructure_pubsub = models.PositiveIntegerField()
    infrastructure_prvsub = models.PositiveIntegerField()
    infrastructure_nacl = models.PositiveIntegerField()
    infrastructure_sg = models.PositiveIntegerField()
    infrastructure_pubinst = models.PositiveIntegerField()
    infrastructure_prvinst = models.PositiveIntegerField()

    def __str__(self):
        return self.infrastructure_name
