# Generated by Django 3.0.4 on 2020-03-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200329_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telephonenb',
            field=models.PositiveIntegerField(db_column='TelephoneNb'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='omra',
            name='distance_from_haram',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='omra',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='omra',
            name='room_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizedjourney',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizedjourney',
            name='room_type',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sum_payment',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='travelhotelreservation',
            name='reservation_number',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='visa',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visa',
            name='single_voyage_field',
            field=models.PositiveIntegerField(blank=True, db_column='single_voyage?', null=True),
        ),
    ]
