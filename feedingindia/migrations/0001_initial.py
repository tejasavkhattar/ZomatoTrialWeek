# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('partnering_entity', models.CharField(max_length=250, null=True)),
                ('institution', models.CharField(max_length=250, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=70, blank=True, null=True)),
                ('designation', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('pincode', models.IntegerField()),
                ('additional', models.CharField(max_length=1000, null=True)),
                ('latitude', models.CharField(max_length=1000, null=True)),
                ('longitude', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('type_of_donation', models.CharField(max_length=250, null=True)),
                ('date_donate', models.CharField(max_length=250, null=True)),
                ('time_donate', models.CharField(max_length=250, null=True)),
                ('food_for_donate', models.IntegerField(null=True)),
                ('counter', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_donator', models.CharField(max_length=250, null=True)),
                ('contact_donator', models.IntegerField(null=True)),
                ('name_shelter', models.CharField(max_length=250, null=True)),
                ('address_shelter', models.CharField(max_length=250, null=True)),
                ('time_delivery', models.CharField(max_length=250, null=True)),
                ('date_delivery', models.CharField(max_length=250, null=True)),
                ('food_for_donate', models.IntegerField(null=True)),
                ('counter', models.IntegerField(null=True)),
            ],
        ),
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
                ('email_incharge', models.EmailField(max_length=70, blank=True, null=True)),
                ('latitude', models.CharField(max_length=1000, null=True)),
                ('longitude', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=70, blank=True, null=True)),
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
