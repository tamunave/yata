# Generated by Django 3.0.4 on 2020-05-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0031_auto_20200525_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abroadstocks',
            name='cost',
            field=models.BigIntegerField(default=0),
        ),
    ]
