# Generated by Django 2.0.5 on 2019-09-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0057_wall_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wall',
            name='result',
            field=models.CharField(default='Unset', max_length=10),
        ),
    ]
