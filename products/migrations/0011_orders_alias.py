# Generated by Django 4.2 on 2023-05-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productvariant_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='alias',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
