# Generated by Django 3.1.4 on 2021-10-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0195_auto_20211003_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='public_secret',
            field=models.CharField(blank=True, default='eiaebcihghihgceehacg', help_text='The secret for the communication with the APX race control', max_length=500),
        ),
        migrations.AlterField(
            model_name='serverplugin',
            name='plugin_path',
            field=models.CharField(blank=True, default=None, help_text='The target folder the file should be placed into', max_length=500, null=True),
        ),
    ]
