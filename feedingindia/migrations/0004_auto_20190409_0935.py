# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedingindia', '0003_shelter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donater',
            name='email',
            field=models.EmailField(max_length=70, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='email_incharge',
            field=models.EmailField(max_length=70, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=70, blank=True, null=True),
        ),
    ]
