# Generated by Django 4.1.7 on 2023-04-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gameuser_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='stage_number',
            field=models.PositiveIntegerField(verbose_name='номер этапа'),
        ),
    ]