# Generated by Django 4.2.6 on 2024-02-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='', max_length=10),
        ),
    ]