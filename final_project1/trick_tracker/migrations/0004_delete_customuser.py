# Generated by Django 4.2.7 on 2023-12-04 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trick_tracker', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]