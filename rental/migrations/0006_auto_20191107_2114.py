# Generated by Django 2.2.6 on 2019-11-07 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_reservation_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='title',
            new_name='author',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='guest',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.Guest'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
