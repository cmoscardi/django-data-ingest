# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 17:12
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('file_metadata', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('file_type', models.TextField(null=True)),
                ('file', models.FileField(upload_to='')),
                ('raw', models.BinaryField(null=True)),
                ('extracted', models.BinaryField(null=True)),
                ('status', models.IntegerField(choices=[(0, 'unreviewed'), (1, 'approved'), (2, 'retired'), (3, 'rejected')], default=0)),
                ('status_changed_at', models.DateTimeField(null=True)),
                ('uploaded_filename', models.CharField(help_text="Name of the file that was uploaded, as it was called on the uploader's system. For display purposes only.", max_length=128)),
                ('serialized_gleaned_data', models.TextField(help_text='The JSON-serialized data from the upload, including information about any rows that failed validation.')),
                ('status_changed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
