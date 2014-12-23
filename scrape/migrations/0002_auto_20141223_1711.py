# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapelog',
            old_name='created',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='scrapelog',
            old_name='modified',
            new_name='modified_date',
        ),
        migrations.AddField(
            model_name='scrapelog',
            name='end_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scrapelog',
            name='pages_detected',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scrapelog',
            name='pages_scraped',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scrapelog',
            name='status',
            field=models.CharField(null=True, blank=True, max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scrapesite',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scrapesite',
            name='url',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
    ]
