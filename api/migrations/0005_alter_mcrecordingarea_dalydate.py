# Generated by Django 4.0 on 2021-12-21 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_mcrecordingarea_dalydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcrecordingarea',
            name='dalydate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mcdailyrecordingarea'),
        ),
    ]
