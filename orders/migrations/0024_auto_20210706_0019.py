# Generated by Django 2.2.10 on 2021-07-06 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_orderr_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderr',
            name='order_id',
        ),
        migrations.AddField(
            model_name='completed_order_ids',
            name='order_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.Orderr'),
        ),
    ]
