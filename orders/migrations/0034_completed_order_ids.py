# Generated by Django 2.2.10 on 2021-07-09 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0033_delete_completed_order_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed_Order_Ids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('order_detail', models.CharField(max_length=800)),
                ('status', models.CharField(choices=[('Initiated', 'Initiated'), ('Completed', 'Completed'), ('Refunded', 'Refunded')], default='Initiated', max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
