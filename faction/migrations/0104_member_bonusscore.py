# Generated by Django 3.1.2 on 2020-12-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0103_auto_20201220_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='bonusScore',
            field=models.IntegerField(default=0),
        ),
    ]
