# Generated by Django 4.2.6 on 2023-11-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_sizes_product_product_color_delete_colors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=10),
        ),
    ]