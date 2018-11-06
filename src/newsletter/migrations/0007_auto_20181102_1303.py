# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-02 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20181101_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ami_type', models.CharField(choices=[('Amazon AMI', 'Amazon Linux AMI 2018.03.0'), ('RedHat', 'Red Hat Entreprise Linux 7.5'), ('Ubuntu Server', 'Ubuntu Server 16.04 LTS')], default='T2.micro', max_length=20)),
                ('instance_type', models.CharField(choices=[('t2.micro', 't2.micro')], default='Amazon Linux AMI 2018.03.0', max_length=20)),
                ('ami_type2', models.CharField(choices=[('Amazon AMI', 'Amazon Linux AMI 2018.03.0'), ('RedHat', 'Red Hat Entreprise Linux 7.5'), ('Ubuntu Server', 'Ubuntu Server 16.04 LTS')], default='T2.micro', max_length=20)),
                ('instance_type2', models.CharField(choices=[('t2.micro', 't2.micro')], default='Amazon Linux AMI 2018.03.0', max_length=20)),
                ('inst_infra', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='nacl',
            name='nacl_out_prot',
            field=models.CharField(choices=[('SSH', 'SSH'), ('ICMP', 'ICMP'), ('HTTP', 'HTTP'), ('ALL', 'ALL')], default='ALL', max_length=20),
        ),
    ]
