# Generated by Django 4.0 on 2021-12-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_machine_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='machine',
            name='machine_status',
            field=models.BooleanField(),
        ),
    ]