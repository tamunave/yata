# Generated by Django 3.0.1 on 2020-02-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0046_auto_20200210_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='daysold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='faction',
            name='maxmembers',
            field=models.IntegerField(default=0),
        ),
    ]
