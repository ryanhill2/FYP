# Generated by Django 3.0.3 on 2020-03-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0031_auto_20200312_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(to='portfolio.Stock'),
        ),
    ]
