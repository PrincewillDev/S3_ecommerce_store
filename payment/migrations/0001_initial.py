# Generated by Django 5.1 on 2024-09-07 10:17

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_method_id', models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_method', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('payment_status_id', models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_status', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='Paymentuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('payment_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentstatus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
