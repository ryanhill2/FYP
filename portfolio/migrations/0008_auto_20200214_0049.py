# Generated by Django 3.0.2 on 2020-02-14 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20200214_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='created',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Stock'),
        ),
    ]
