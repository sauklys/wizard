# Generated by Django 3.1.4 on 2021-09-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0172_auto_20210903_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='remove_settings',
            field=models.BooleanField(default=False, help_text='Decides if APX will remove the content of the settings folder. If you plan to rely on autosave grip files, do not check this option', verbose_name='remove settings folder'),
        ),
        migrations.AlterField(
            model_name='server',
            name='public_secret',
            field=models.CharField(blank=True, default='bdehdbfgbbbedbddcgbb', help_text='The secret for the communication with the APX race control', max_length=500),
        ),
    ]
