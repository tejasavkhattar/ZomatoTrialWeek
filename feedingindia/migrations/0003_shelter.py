# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedingindia', '0002_donater'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_hunger_spot', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('pincode', models.IntegerField()),
                ('total_benefitiaries', models.IntegerField()),
                ('type_shelter', models.CharField(max_length=100, null=True)),
                ('raw_food', models.CharField(max_length=250, null=True)),
                ('cooked_food', models.CharField(max_length=250, null=True)),
                ('preference', models.CharField(max_length=250, null=True)),
                ('time_range', models.CharField(max_length=250, null=True)),
                ('heat_food', models.CharField(max_length=250, null=True)),
                ('refrigerate_food', models.CharField(max_length=250, null=True)),
                ('external_support', models.CharField(max_length=250, null=True)),
                ('support', models.CharField(max_length=250, null=True)),
                ('reg_status', models.CharField(max_length=250, null=True)),
                ('name_incharge', models.CharField(max_length=250, null=True)),
                ('contact_incharge', models.CharField(max_length=250, null=True)),
                ('email_incharge', models.EmailField(max_length=70, blank=True)),
                ('latitude', models.CharField(max_length=1000, null=True)),
                ('longitude', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
