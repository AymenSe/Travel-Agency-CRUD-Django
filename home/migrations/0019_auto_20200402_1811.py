# Generated by Django 3.0.4 on 2020-04-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200401_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omra',
            name='food_field',
            field=models.BooleanField(default=True),
        ),
    ]