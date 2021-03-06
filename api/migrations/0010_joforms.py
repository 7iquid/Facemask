# Generated by Django 4.0 on 2022-06-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_mcrecordingarea_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoForms',
            fields=[
                ('MotheJO', models.CharField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('RefPoNo', models.CharField(max_length=300, null=True)),
                ('RefQtnNo', models.CharField(max_length=300, null=True)),
                ('RefDrawingNo', models.CharField(max_length=300, null=True)),
                ('Customer', models.CharField(max_length=300, null=True)),
                ('PoDate', models.CharField(max_length=300, null=True)),
                ('DateIssued', models.CharField(max_length=300, null=True)),
                ('CompletionDateInPo', models.CharField(max_length=300, null=True)),
                ('DeliveryDateToCustomer', models.CharField(max_length=300, null=True)),
                ('SalesInCharge', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
