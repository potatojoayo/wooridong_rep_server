# Generated by Django 4.0.5 on 2023-02-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee', '0004_delete_buildingfee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitbill',
            name='date_created',
            field=models.DateField(),
        ),
    ]
