# Generated by Django 2.2.13 on 2023-09-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreGames', '0006_auto_20230915_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechanacimiento',
            field=models.DateField(),
        ),
    ]
