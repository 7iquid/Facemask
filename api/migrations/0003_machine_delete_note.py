# Generated by Django 4.0 on 2021-12-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211205_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('machine_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
