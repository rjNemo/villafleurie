# Generated by Django 2.2.6 on 2019-11-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20191106_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='max_occupation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='surface',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]