# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField


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

class NACL(models.Model):
    nacl_name = models.CharField(max_length=20)
    nacl_src_ip = models.GenericIPAddressField()
    nacl_in_prot = models.CharField(max_length=20)
    nacl_out_prot = models.CharField(max_length=20)

    def __str__(self):
        return self.nacl_name

class SG(models.Model):
    sg_name = models.CharField(max_length=20)
    sg_src_ip = models.GenericIPAddressField()
    sg_in_prot = models.CharField(max_length=20)
    sg_out_prot = models.CharField(max_length=20)

    def __str__(self):
        return self.sg_name

class Instance(models.Model):
    INST_TYPE_CHOICES = (
        (".micro", "T2.micro"),
        ("small", "T2.small"),
        ("tiny", "T2.tiny"),
    )
    AMI_CHOICES = (
        ("Amazon AMI", "Amazon Linux AMI 2018.03.0"),
        ("RedHat", "Red Hat Entreprise Linux 7.5"),
        ("Ubuntu Server", "Ubuntu Server 16.04 LTS"),
    )
    ami_type = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
