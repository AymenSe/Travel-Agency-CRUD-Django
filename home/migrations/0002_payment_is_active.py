# Generated by Django 3.0.4 on 2020-08-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
