# Generated by Django 4.2.6 on 2023-10-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_colors_options_alter_sizes_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='size',
            field=models.CharField(max_length=5),
        ),
    ]
