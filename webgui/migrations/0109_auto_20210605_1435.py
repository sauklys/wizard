# Generated by Django 3.1.4 on 2021-06-05 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0108_auto_20210605_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='racesessions',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webgui.track'),
        ),
        migrations.AlterField(
            model_name='server',
            name='public_secret',
            field=models.CharField(blank=True, default='fdddciiibegffbaidcbf', help_text='The secret for the communication with the APX race control', max_length=500),
        ),
    ]
