# Generated by Django 4.0 on 2021-12-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_mcrecordingarea_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcrecordingarea',
            name='by',
            field=models.CharField(default='Name', max_length=20),
        ),
    ]
