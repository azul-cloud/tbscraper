# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0002_auto_20141223_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapelog',
            name='message',
            field=models.CharField(null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
