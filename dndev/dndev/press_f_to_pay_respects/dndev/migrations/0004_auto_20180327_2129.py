# Generated by Django 2.0.3 on 2018-03-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndev', '0003_auto_20180327_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='copper',
            field=models.BigIntegerField(default=0, help_text='Enter the amount of copper for this character'),
        ),
        migrations.AddField(
            model_name='character',
            name='gold',
            field=models.BigIntegerField(default=0, help_text='Enter the amount of gold for this character'),
        ),
        migrations.AddField(
            model_name='character',
            name='silver',
            field=models.BigIntegerField(default=0, help_text='Enter the amount of silver for this character'),
        ),
        migrations.AddField(
            model_name='characterclass',
            name='descrtiption',
            field=models.CharField(default='', help_text='Enter a description of this class', max_length=1000),
        ),
        migrations.AddField(
            model_name='characterclass',
            name='hitpoints',
            field=models.PositiveIntegerField(default=10, help_text='Enter the hit points for this character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.PositiveSmallIntegerField(default=1, help_text='Enter the level your character'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(default='', help_text='Enter a name for your character', max_length=30),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of this class', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of this race', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subrace',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of the subrace', max_length=100, primary_key=True, serialize=False),
        ),
    ]