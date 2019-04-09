# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('pincode', models.IntegerField()),
                ('age', models.IntegerField()),
                ('institution', models.CharField(max_length=250, null=True)),
                ('educational_background', models.CharField(max_length=250, null=True)),
                ('contribution_time', models.CharField(max_length=250, null=True)),
                ('why_join', models.CharField(max_length=1000, null=True)),
                ('latitude', models.CharField(max_length=1000, null=True)),
                ('longitude', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
