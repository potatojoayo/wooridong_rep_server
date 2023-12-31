# Generated by Django 4.0.5 on 2023-02-08 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
        ('villa', '0001_initial'),
        ('fee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villafee',
            name='villa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villa_fees', to='villa.villa'),
        ),
        migrations.AddField(
            model_name='unitfee',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.building'),
        ),
        migrations.AddField(
            model_name='unitfee',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fee.feetype'),
        ),
        migrations.AddField(
            model_name='unitfee',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_fees', to='villa.unit'),
        ),
        migrations.AddField(
            model_name='unitfee',
            name='unit_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_fees', to='fee.unitbill'),
        ),
        migrations.AddField(
            model_name='unitfee',
            name='villa_fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_fees', to='fee.villafee'),
        ),
        migrations.AddField(
            model_name='unitbill',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_bills', to='villa.unit'),
        ),
        migrations.AddField(
            model_name='unitbill',
            name='villa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_bills', to='villa.villa'),
        ),
        migrations.AddField(
            model_name='sentvillafee',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bank.bank'),
        ),
        migrations.AddField(
            model_name='sentvillafee',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_villa_fee', to='fee.feetype'),
        ),
        migrations.AddField(
            model_name='sentvillafee',
            name='impose_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='fee.imposetype'),
        ),
        migrations.AddField(
            model_name='sentvillafee',
            name='villa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_villa_fees', to='villa.villa'),
        ),
        migrations.AddField(
            model_name='sentvillafee',
            name='villa_fee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='sent_villa_fee', to='fee.villafee'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.building'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fee.feetype'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='sent_unit_bill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_unit_fees', to='fee.sentunitbill'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='sent_villa_fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_unit_fees', to='fee.sentvillafee'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_unit_fees', to='villa.unit'),
        ),
        migrations.AddField(
            model_name='sentunitfee',
            name='unit_fee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='sent_unit_fee', to='fee.unitfee'),
        ),
        migrations.AddField(
            model_name='sentunitbill',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_unit_bills', to='villa.unit'),
        ),
        migrations.AddField(
            model_name='sentunitbill',
            name='unit_bill',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='sent_unit_bill', to='fee.unitbill'),
        ),
        migrations.AddField(
            model_name='sentunitbill',
            name='villa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_unit_bills', to='villa.villa'),
        ),
        migrations.AddField(
            model_name='interimsettlement',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.unit'),
        ),
        migrations.AddField(
            model_name='interimsettlement',
            name='unit_bill',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='interim_settlements', to='fee.unitbill'),
        ),
        migrations.AddField(
            model_name='imposefeeonunit',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.building'),
        ),
        migrations.AddField(
            model_name='imposefeeonunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.unit'),
        ),
        migrations.AddField(
            model_name='imposefeeonunit',
            name='villa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.villa'),
        ),
        migrations.AddField(
            model_name='imposefeeonunit',
            name='villa_fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imposing_units', to='fee.villafee'),
        ),
        migrations.AddField(
            model_name='buildingfee',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.building'),
        ),
        migrations.AddField(
            model_name='buildingfee',
            name='fee_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fee.feetype'),
        ),
        migrations.AlterUniqueTogether(
            name='imposefeeonunit',
            unique_together={('villa', 'building', 'unit', 'villa_fee')},
        ),
    ]
