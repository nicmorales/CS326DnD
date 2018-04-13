# Generated by Django 2.0.2 on 2018-04-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndpal', '0006_auto_20180412_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='cName',
            new_name='char_name',
        ),
        migrations.AlterField(
            model_name='subracefeatures',
            name='name',
            field=models.CharField(default='', help_text='Enter the name of the subrace', max_length=100, primary_key=True),
        ),
    ]