# Generated by Django 3.0.2 on 2020-04-30 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artalk_base', '0014_auto_20200430_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='msUserDisLikeCount',
            new_name='cmDisLikeCount',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='msUserLikeCount',
            new_name='cmLikeCount',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='msUserDisLikeCount',
            new_name='msDisLikeCount',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='msUserLikeCount',
            new_name='msLikeCount',
        ),
    ]