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
    # infrastructure_pubsub = models.PositiveIntegerField()
    # infrastructure_prvsub = models.PositiveIntegerField()
    INFRA_NACL = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
    )
    INFRA_SG = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
    )
    INFRA_INST = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
    )
    infrastructure_nacl = models.CharField(max_length = 20, default="1", choices = INFRA_NACL)
    infrastructure_sg = models.CharField(max_length = 20, default="1", choices = INFRA_SG)
    infrastructure_pubinst = models.CharField(max_length = 20, default="1", choices = INFRA_INST)

    def __str__(self):
        return self.infrastructure_name

class NACL(models.Model):
    nacl_name = models.CharField(max_length=20)
    nacl_owner = models.ForeignKey(User,default=None)
    NACL_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    NACL_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    nacl_in_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_infra = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nacl_infra+" "+"nacl"

class NACL2(models.Model):
    nacl_name = models.CharField(max_length=20)
    nacl_owner = models.ForeignKey(User,default=None)
    NACL_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    NACL_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    nacl_in_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_infra = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nacl_infra+" "+"nacl"

class NACL3(models.Model):
    nacl_name = models.CharField(max_length=20)
    nacl_owner = models.ForeignKey(User,default=None)
    NACL_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    NACL_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    nacl_in_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot3 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot3 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_infra = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nacl_infra+" "+"nacl"

class NACL4(models.Model):
    nacl_name = models.CharField(max_length=20)
    nacl_owner = models.ForeignKey(User,default=None)
    NACL_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    NACL_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    nacl_in_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot3 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot3 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_in_prot4 = models.CharField(max_length = 20, default="ALL", choices = NACL_IN_PROT)
    nacl_out_prot4 = models.CharField(max_length = 20, default="ALL", choices = NACL_OUT_PROT)
    nacl_infra = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.nacl_infra+" "+"nacl"

class SG(models.Model):
    sg_name = models.CharField(max_length=20)
    sg_owner = models.ForeignKey(User,default=None)

    SG_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    SG_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    sg_in_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_infra = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.sg_infra+" "+"sg"

class SG2(models.Model):
    sg_name = models.CharField(max_length=20)
    sg_owner = models.ForeignKey(User,default=None)
    SG_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    SG_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    sg_in_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_infra = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.sg_infra+" "+"sg"

class SG3(models.Model):
    sg_name = models.CharField(max_length=20)
    sg_owner = models.ForeignKey(User,default=None)
    SG_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    SG_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    sg_in_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot3 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot3 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_infra = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.sg_infra+" "+"sg"

class SG4(models.Model):
    sg_name = models.CharField(max_length=20)
    sg_owner = models.ForeignKey(User,default=None)
    SG_IN_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    SG_OUT_PROT = (
        ("SSH","SSH"),
        ("ICMP","ICMP"),
        ("HTTP","HTTP"),
        ("ALL","ALL")
    )
    sg_in_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot2 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot3 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot3 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_in_prot4 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_out_prot4 = models.CharField(max_length = 20, default="ALL", choices = SG_IN_PROT)
    sg_infra = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.sg_infra+" "+"sg"

class Instance(models.Model):
    INST_TYPE_CHOICES = (
        ("t2.micro", "t2.micro"),
    )
    AMI_CHOICES = (
        ("Amazon AMI", "Amazon Linux AMI 2018.03.0"),
        ("RedHat", "Red Hat Entreprise Linux 7.5"),
        ("Ubuntu Server", "Ubuntu Server 16.04 LTS"),
    )
    ami_type = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    inst_infra = models.CharField(max_length=20,default="")
    inst_owner = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.inst_infra+" "+"instance"

class Instance2(models.Model):
    INST_TYPE_CHOICES = (
        ("t2.micro", "t2.micro"),
    )
    AMI_CHOICES = (
        ("Amazon AMI", "Amazon Linux AMI 2018.03.0"),
        ("RedHat", "Red Hat Entreprise Linux 7.5"),
        ("Ubuntu Server", "Ubuntu Server 16.04 LTS"),
    )
    ami_type = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type2 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type2 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    inst_infra = models.CharField(max_length=20,default="")
    inst_owner = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.inst_infra+" "+"instance"

class Instance3(models.Model):
    INST_TYPE_CHOICES = (
        ("t2.micro", "t2.micro"),
    )
    AMI_CHOICES = (
        ("Amazon AMI", "Amazon Linux AMI 2018.03.0"),
        ("RedHat", "Red Hat Entreprise Linux 7.5"),
        ("Ubuntu Server", "Ubuntu Server 16.04 LTS"),
    )
    ami_type = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type2 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type2 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type3 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type3 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    inst_infra = models.CharField(max_length=20,default="")
    inst_owner = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.inst_infra+" "+"instance"

class Instance4(models.Model):
    INST_TYPE_CHOICES = (
        ("t2.micro", "t2.micro"),
    )
    AMI_CHOICES = (
        ("Amazon AMI", "Amazon Linux AMI 2018.03.0"),
        ("RedHat", "Red Hat Entreprise Linux 7.5"),
        ("Ubuntu Server", "Ubuntu Server 16.04 LTS"),
    )
    ami_type = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type2 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type2 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type3 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type3 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    ami_type4 = models.CharField(max_length = 20, default="T2.micro", choices = AMI_CHOICES)
    instance_type4 = models.CharField(max_length = 20,default="Amazon Linux AMI 2018.03.0", choices = INST_TYPE_CHOICES)
    inst_infra = models.CharField(max_length=20,default="")
    inst_owner = models.ForeignKey(User,default=None)
    def __str__(self):
        return self.inst_infra+" "+"instance"
