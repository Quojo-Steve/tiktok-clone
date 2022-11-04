# Generated by Django 4.0.5 on 2022-10-28 13:52

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_newuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoupload',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videoupload',
            name='user',
            field=models.CharField(default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='videoupload',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='videoupload',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
