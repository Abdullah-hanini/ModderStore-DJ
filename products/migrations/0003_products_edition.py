# Generated by Django 4.2 on 2023-04-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='edition',
            field=models.CharField(choices=[('Standard Edtion', 'Standard Edtion'), ('Deluxe Edtion', 'Deluxe Edtion'), ('Ultimate Edtion', 'Ultimate Edtion')], default='Standard Edtion', max_length=50),
            preserve_default=False,
        ),
    ]
