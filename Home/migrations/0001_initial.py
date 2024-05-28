# Generated by Django 5.0.6 on 2024-05-28 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField()),
                ('Reguler_balance', models.IntegerField(null=True)),
                ('Primium_balance', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription_nowcook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Premium', 'Premium')], max_length=20, null=True)),
                ('plan', models.IntegerField(blank=True, choices=[(3, '3 Days'), (7, '7 Days'), (15, '15 Days'), (30, '30 Days')], null=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_lunch_off', models.BooleanField(default=False)),
                ('is_dinner_off', models.BooleanField(default=False)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('Primium_balance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='premium_subscriptions', to='Home.plan')),
                ('Reguler_balance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regular_subscriptions', to='Home.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
