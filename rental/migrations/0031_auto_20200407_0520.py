# Generated by Django 3.0.4 on 2020-04-07 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0030_auto_20200331_0439'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservation',
            new_name='Booking',
        ),
        migrations.RenameModel(
            old_name='Image',
            new_name='Picture',
        ),
    ]