# Generated by Django 3.0 on 2019-12-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0024_auto_20191203_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='calendar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
