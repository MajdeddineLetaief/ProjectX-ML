# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-03 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_sg3'),
    ]

    operations = [
        migrations.CreateModel(
            name='NACL3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nacl_name', models.CharField(max_length=20)),
                ('nacl_in_prot', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_out_prot', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTP', 'HTTP'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_in_prot2', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_out_prot2', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTP', 'HTTP'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_in_prot3', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTPS', 'HTTPS'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_out_prot3', models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTP', 'HTTP'), ('ALL', 'ALL')], default='ALL', max_length=20)),
                ('nacl_infra', models.CharField(default='', max_length=20)),
            ],
        ),
    ]