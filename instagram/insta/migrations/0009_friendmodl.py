# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-11 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_timelinemodl'),
    ]

    operations = [
        migrations.CreateModel(
            name='friendmodl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_No', models.IntegerField()),
                ('Friend_No', models.IntegerField()),
                ('Request_status', models.BooleanField(default=False)),
                ('Friend_status', models.BooleanField(default=False)),
            ],
        ),
    ]
