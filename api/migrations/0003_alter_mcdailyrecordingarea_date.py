# Generated by Django 4.0 on 2021-12-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_machine_mcdailyrecordingarea_mcrecordingarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcdailyrecordingarea',
            name='date',
            field=models.DateTimeField(primary_key=True, serialize=False, unique=True),
        ),
    ]
