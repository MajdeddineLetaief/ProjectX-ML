# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-31 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20181031_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacl',
            name='nacl_in_prot',
            field=models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20),
        ),
        migrations.AlterField(
            model_name='nacl',
            name='nacl_out_prot',
            field=models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20),
        ),
        migrations.AlterField(
            model_name='sg',
            name='sg_in_prot',
            field=models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20),
        ),
        migrations.AlterField(
            model_name='sg',
            name='sg_out_prot',
            field=models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20),
        ),
    ]
