# Generated by Django 2.2.6 on 2019-11-10 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0012_auto_20191110_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.Place'),
        ),
    ]
