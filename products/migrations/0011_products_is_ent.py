# Generated by Django 4.2 on 2023-05-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_products_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_ent',
            field=models.BooleanField(default=False),
        ),
    ]