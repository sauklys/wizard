# Generated by Django 3.1.4 on 2021-10-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0192_auto_20211002_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverplugin',
            name='plugin_path',
            field=models.CharField(blank=True, default='', help_text='The target folder the file should be placed into', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='public_secret',
            field=models.CharField(blank=True, default='igabdhdeeghgdbicaibi', help_text='The secret for the communication with the APX race control', max_length=500),
        ),
        migrations.AlterField(
            model_name='servercron',
            name='disabled',
            field=models.BooleanField(default=False, help_text='Disables the job'),
        ),
        migrations.AlterField(
            model_name='servercron',
            name='modifier',
            field=models.IntegerField(default=1, help_text='Repeat the job each X minutes, a value of 1 means no repeat', verbose_name='Repeat'),
        ),
    ]
