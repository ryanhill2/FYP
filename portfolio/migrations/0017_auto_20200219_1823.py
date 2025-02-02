# Generated by Django 3.0.2 on 2020-02-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20200219_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(to='portfolio.Stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='number_of_shares',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_price',
            field=models.TextField(blank=True, max_length=10),
        ),
    ]
