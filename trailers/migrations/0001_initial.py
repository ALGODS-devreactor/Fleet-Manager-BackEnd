# Generated by Django 3.2.7 on 2021-09-14 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('year', models.IntegerField()),
                ('unit_tracking', models.IntegerField()),
                ('make', models.CharField(blank=True, max_length=100)),
                ('VIN_number', models.IntegerField()),
                ('plate_number', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('weight_pounds', models.FloatField()),
                ('value', models.FloatField()),
                ('still_working', models.BooleanField(default=False)),
                ('leave_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TrailerSafetyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_detail', models.CharField(blank=True, max_length=100)),
                ('renewal_date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=100)),
                ('stop_dispatch_on_expiry', models.BooleanField(default=False)),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trailers.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerRepairService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type_service', models.CharField(blank=True, max_length=100)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trailers.trailer')),
            ],
        ),
        migrations.CreateModel(
            name='TrailerMonthlyDeduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_deduction', models.CharField(blank=True, max_length=100)),
                ('day_of_month', models.IntegerField()),
                ('currency_CDN', models.BooleanField(default=False)),
                ('charges', models.FloatField()),
                ('valid_till', models.DateField()),
                ('vendor', models.CharField(blank=True, max_length=100)),
                ('HST', models.BooleanField(default=False)),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trailers.trailer')),
            ],
        ),
    ]