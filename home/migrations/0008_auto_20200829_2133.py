# Generated by Django 3.0.4 on 2020-08-29 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200828_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='ticket',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]