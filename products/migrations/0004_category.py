# Generated by Django 4.2 on 2023-04-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_edition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
