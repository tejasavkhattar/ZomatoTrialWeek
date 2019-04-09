# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedingindia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('partnering_entity', models.CharField(max_length=250, null=True)),
                ('institution', models.CharField(max_length=250, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('designation', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('pincode', models.IntegerField()),
                ('additional', models.CharField(max_length=1000, null=True)),
                ('latitude', models.CharField(max_length=1000, null=True)),
                ('longitude', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
