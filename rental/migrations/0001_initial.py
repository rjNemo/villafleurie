# Generated by Django 2.2.6 on 2019-11-06 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Voyageur',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('pictures', models.ImageField(
                    blank=True, null=True, upload_to='uploads/')),
                ('decription', models.TextField(blank=True)),
                ('tagline', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(
                    decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'verbose_name': 'Appartement',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='rental.Guest')),
                ('place', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='rental.Place')),
            ],
            options={
                'verbose_name': 'Réservation',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('reservation', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='rental.Reservation')),
            ],
            options={
                'verbose_name': 'Témoignage',
            },
        ),
    ]