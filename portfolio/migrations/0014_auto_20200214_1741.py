# Generated by Django 3.0.2 on 2020-02-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20200214_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(to='portfolio.Stock'),
        ),
    ]
