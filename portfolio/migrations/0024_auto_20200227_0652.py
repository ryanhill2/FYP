# Generated by Django 3.0.3 on 2020-02-27 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20200227_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Stock'),
        ),
    ]
