# Generated by Django 3.2.7 on 2021-09-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='driver',
            field=models.ManyToManyField(to='drivers.Driver'),
        ),
    ]