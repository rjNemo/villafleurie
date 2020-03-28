# Generated by Django 2.2.6 on 2019-11-11 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0018_auto_20191111_0912'),
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