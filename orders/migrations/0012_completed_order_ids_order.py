# Generated by Django 2.2.10 on 2021-05-31 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_delete_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed_Order_Ids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('status', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ManyToManyField(blank=True, related_name='item', to='orders.ItemCost')),
                ('item_topping', models.ManyToManyField(blank=True, related_name='item_topping', to='orders.Topping')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.Completed_Order_Ids')),
            ],
            options={
                'get_latest_by': ['item'],
            },
        ),
    ]
