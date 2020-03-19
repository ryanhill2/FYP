# Generated by Django 3.0.3 on 2020-03-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_remove_portfolio_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='portfolioCreated',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='portfolioUpdated',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stockCreated',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stockUpdated',
            new_name='updated',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='daily_adj_close',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='daily_close',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='daily_high',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='daily_low',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='daily_open',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock_volume',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='date',
            field=models.TextField(default=11, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='stocks',
            field=models.ManyToManyField(to='portfolio.Stock'),
        ),
    ]
