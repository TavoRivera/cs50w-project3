# Generated by Django 2.2.10 on 2021-07-06 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20210604_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed_order_ids',
            name='order_id',
        ),
    ]
