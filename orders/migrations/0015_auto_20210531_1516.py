# Generated by Django 2.2.10 on 2021-05-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20210531_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderr',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
