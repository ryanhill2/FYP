# Generated by Django 3.0.2 on 2020-02-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200204_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
