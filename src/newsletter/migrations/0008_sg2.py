# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-03 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20181102_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='SG2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sg_name', models.CharField(max_length=20)),
                ('sg_in_prot', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('sg_out_prot', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('sg_in_prot2', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('sg_out_prot2', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('sg_infra', models.CharField(default='', max_length=20)),
            ],
        ),
    ]