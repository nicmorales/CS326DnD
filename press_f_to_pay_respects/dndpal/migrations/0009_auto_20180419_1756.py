# Generated by Django 2.0.2 on 2018-04-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0008_auto_20180412_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subracefeatures',
            name='name',
        ),
        migrations.AddField(
            model_name='characterclass',
            name='skill_options',
            field=models.CharField(default='', help_text='Enter a comma separated spell list. Ex: {"sneak", "toxic"}', max_length=100),
        ),
        migrations.AddField(
            model_name='characterclassspelllist',
            name='spell_list',
            field=models.CharField(default='', help_text='Enter a comma separated spell list. Ex: {"pew", "explosiioonnn"}', max_length=10000),
        ),
        migrations.AddField(
            model_name='charactersubclassspelllist',
            name='spell_list',
            field=models.CharField(default='', help_text='Enter a comma separated spell list. Ex: {"pew", "explosiioonnn"}', max_length=10000),
        ),
        migrations.AddField(
            model_name='subrace',
            name='modifiers',
            field=models.CharField(default='', help_text='Enter the stats modifiers in JSON format. Ex: {"str": 2, "dex": 8}', max_length=20),
        ),
        migrations.AlterField(
            model_name='armor',
            name='is_stealth',
            field=models.BooleanField(default=False, help_text='Is the armor stealthy?'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='max_dexterity',
            field=models.SmallIntegerField(default=0, help_text='Enter the maximum amount of bonus AC from dex modifier.'),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='hitpoints',
            field=models.PositiveIntegerField(default=10, help_text='Enter the hit points for this class'),
        ),
    ]
