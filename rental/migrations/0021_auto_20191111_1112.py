# Generated by Django 2.2.6 on 2019-11-11 11:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0020_auto_20191111_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='start',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
