# Generated by Django 3.0.2 on 2020-05-19 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artalk_base', '0022_auto_20200519_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cmTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 21, 41, 9, 813820)),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='disLikeTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 21, 41, 9, 813820)),
        ),
        migrations.AlterField(
            model_name='like',
            name='likeTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 21, 41, 9, 813820)),
        ),
        migrations.AlterField(
            model_name='message',
            name='msTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 21, 41, 9, 812822)),
        ),
    ]
