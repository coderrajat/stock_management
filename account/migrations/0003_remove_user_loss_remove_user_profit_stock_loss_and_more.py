# Generated by Django 4.0 on 2023-10-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_order_placed_stock_user_loss_user_profit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='loss',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profit',
        ),
        migrations.AddField(
            model_name='stock',
            name='loss',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='profit',
            field=models.IntegerField(default=0),
        ),
    ]
