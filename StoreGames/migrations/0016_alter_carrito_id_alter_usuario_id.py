# Generated by Django 4.2.5 on 2023-10-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreGames', '0015_carrito_precio_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
