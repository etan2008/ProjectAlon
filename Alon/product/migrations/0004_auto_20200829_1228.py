# Generated by Django 3.1 on 2020-08-29 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200828_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuoyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=220)),
                ('municipality', models.CharField(max_length=220)),
                ('barangay', models.CharField(max_length=220)),
                ('buoy_number', models.PositiveIntegerField()),
                ('id_number', models.CharField(max_length=220)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Fisherman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=220)),
                ('municipality', models.CharField(max_length=220)),
                ('barangay', models.CharField(max_length=220)),
                ('id_number', models.CharField(max_length=220)),
                ('name', models.CharField(max_length=220)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='intruder',
            name='recognized',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]