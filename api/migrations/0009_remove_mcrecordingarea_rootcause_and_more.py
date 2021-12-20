# Generated by Django 4.0 on 2021-12-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_machine_id_mcrecordingarea_rootcause_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcrecordingarea',
            name='rootcause',
        ),
        migrations.AddField(
            model_name='mcrecordingarea',
            name='root_cause',
            field=models.CharField(default='Root Cause', max_length=300),
        ),
        migrations.AlterField(
            model_name='mcrecordingarea',
            name='action_taken',
            field=models.CharField(default='Action Taken', max_length=300),
        ),
    ]