# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BBL', models.IntegerField()),
                ('dateBuilt', models.IntegerField()),
                ('address', models.TextField(max_length=30)),
            ],
        ),
    ]
