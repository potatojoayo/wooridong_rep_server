# Generated by Django 4.0.5 on 2023-02-10 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0003_rename_date_unitfee_date_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuildingFee',
        ),
    ]
