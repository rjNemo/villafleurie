# Generated by Django 2.2.7 on 2019-12-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0022_auto_20191111_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='quotation',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
