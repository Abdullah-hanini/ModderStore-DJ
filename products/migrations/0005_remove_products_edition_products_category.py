# Generated by Django 4.2 on 2023-04-26 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='edition',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
            preserve_default=False,
        ),
    ]
