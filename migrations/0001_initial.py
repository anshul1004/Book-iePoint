# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('num_copies', models.IntegerField(default=0)),
            ],
        ),
    ]
