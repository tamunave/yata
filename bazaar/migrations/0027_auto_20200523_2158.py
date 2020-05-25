# Generated by Django 3.0.4 on 2020-05-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0026_abroadstocks_last'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abroadstocks',
            name='country_id',
        ),
        migrations.AddField(
            model_name='abroadstocks',
            name='country_key',
            field=models.CharField(default='???', max_length=3),
        ),
    ]