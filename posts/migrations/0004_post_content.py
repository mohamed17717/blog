# Generated by Django 2.2 on 2020-09-24 05:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_seen_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
