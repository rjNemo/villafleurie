# Generated by Django 2.2.6 on 2019-11-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_auto_20191107_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
