# Generated by Django 3.0.1 on 2020-02-26 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0054_auto_20200224_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttacksPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField(default=0)),
                ('player_name', models.CharField(blank=True, default='player_name', max_length=16, null=True)),
                ('hits', models.IntegerField(default=0)),
                ('attacks', models.IntegerField(default=0)),
                ('defends', models.IntegerField(default=0)),
                ('attacked', models.IntegerField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faction.AttacksReport')),
            ],
        ),
        migrations.CreateModel(
            name='AttacksFaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction_id', models.IntegerField(default=0)),
                ('faction_name', models.CharField(blank=True, default='faction_name', max_length=64, null=True)),
                ('wins', models.IntegerField(default=0)),
                ('attacks', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('show', models.BooleanField(default=False)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faction.AttacksReport')),
            ],
        ),
    ]
