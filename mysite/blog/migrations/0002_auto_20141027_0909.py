# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'blogPhotos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='post_summary',
            field=models.TextField(default=b"Don't leave blank"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='post_text',
            field=models.TextField(default=b"Don't leave blank"),
            preserve_default=True,
        ),
    ]
