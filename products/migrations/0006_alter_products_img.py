# Generated by Django 4.2 on 2023-04-29 11:18

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_products_edition_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to=products.models.imgup),
        ),
    ]
