# Generated by Django 4.0 on 2022-01-28 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_categoriasdeproducto_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalindicadoresdeoferta',
            old_name='categoy_product',
            new_name='category_product',
        ),
        migrations.RenameField(
            model_name='historicalproducto',
            old_name='categoy_product',
            new_name='category_product',
        ),
        migrations.RenameField(
            model_name='indicadoresdeoferta',
            old_name='categoy_product',
            new_name='category_product',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categoy_product',
            new_name='category_product',
        ),
    ]
