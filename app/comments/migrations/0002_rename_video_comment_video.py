# Generated by Django 5.0.3 on 2024-03-21 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Video',
            new_name='video',
        ),
    ]
