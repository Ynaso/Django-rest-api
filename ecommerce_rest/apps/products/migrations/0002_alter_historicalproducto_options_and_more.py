# Generated by Django 4.2.3 on 2023-07-16 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalproducto',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Producto', 'verbose_name_plural': 'historical Productos'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproducto',
            name='CategoryProduct',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct', verbose_name='Categoria de producto'),
        ),
        migrations.AddField(
            model_name='historicalproducto',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Unidad de medida'),
        ),
        migrations.AddField(
            model_name='producto',
            name='CategoryProduct',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoria de producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de medida'),
        ),
    ]
