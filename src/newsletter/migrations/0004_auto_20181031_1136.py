# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-31 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20181030_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customstack',
            name='infrastructure_nacl',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='customstack',
            name='infrastructure_pubinst',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='customstack',
            name='infrastructure_sg',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='instance',
            name='instance_type',
            field=models.CharField(choices=[('t2.micro', 't2.micro'), ('t2.small', 't2.small'), ('t2.tiny', 't2.tiny')], default='Amazon Linux AMI 2018.03.0', max_length=20),
        ),
    ]
