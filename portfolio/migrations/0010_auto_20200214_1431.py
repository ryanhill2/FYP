# Generated by Django 3.0.2 on 2020-02-14 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20200214_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Stock'),
        ),
    ]
