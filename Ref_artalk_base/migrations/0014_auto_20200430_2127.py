# Generated by Django 3.0.2 on 2020-04-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artalk_base', '0013_auto_20200430_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msCx',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='message',
            name='msCy',
            field=models.FloatField(default=0),
        ),
    ]
