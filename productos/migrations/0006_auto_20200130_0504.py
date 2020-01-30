# Generated by Django 3.0.2 on 2020-01-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20200130_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=40, unique=True)),
                ('irri1', models.CharField(blank=True, max_length=40)),
                ('irri2', models.CharField(blank=True, max_length=40)),
                ('irri3', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=40, unique=True)),
                ('soil1', models.CharField(blank=True, max_length=40)),
                ('soil2', models.CharField(blank=True, max_length=40)),
                ('soil3', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='crop2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='producto',
            name='crop3',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]