# Generated by Django 4.0.5 on 2023-02-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_type', models.IntegerField(choices=[(0, 'All'), (1, 'Building'), (2, 'Unit'), (3, 'Rep'), (4, 'Push')])),
                ('notification_type', models.IntegerField(choices=[(0, 'Pay Villa Fee'), (1, 'Unit Bill Paid'), (2, 'Send Bill'), (3, 'Before Pay Villa Fee'), (4, 'Villa Fee Register Success'), (5, 'Villa Fee Register Failed')])),
                ('message', models.TextField()),
                ('contents', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('read_datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
