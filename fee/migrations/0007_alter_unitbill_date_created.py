# Generated by Django 4.0.5 on 2023-04-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0006_remove_unitbill_interim_settlement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitbill',
            name='date_created',
            field=models.DateField(),
        ),
    ]