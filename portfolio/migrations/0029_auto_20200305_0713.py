# Generated by Django 3.0.3 on 2020-03-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_auto_20200304_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='current_price',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(to='portfolio.Stock'),
        ),
    ]
