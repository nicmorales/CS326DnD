# Generated by Django 2.0.4 on 2018-04-28 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0013_auto_20180426_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='weapon',
        ),
        migrations.DeleteModel(
            name='Properties',
        ),
    ]