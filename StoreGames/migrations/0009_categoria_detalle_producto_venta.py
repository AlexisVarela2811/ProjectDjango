# Generated by Django 2.2.13 on 2023-09-29 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreGames', '0008_auto_20230920_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la categoria')),
                ('nombreCat', models.CharField(max_length=30, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de venta')),
                ('fechaVenta', models.DateField(verbose_name='Id de venta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio del Producto')),
                ('descripcionProducto', models.CharField(max_length=900, verbose_name='Descripcion del Producto')),
                ('stockProd', models.IntegerField(verbose_name='Stock del Producto')),
                ('catergoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreGames.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del detalle')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('subTotal', models.IntegerField(verbose_name='Subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreGames.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreGames.Venta')),
            ],
        ),
    ]
