# Generated by Django 3.0.4 on 2020-03-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0028_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
