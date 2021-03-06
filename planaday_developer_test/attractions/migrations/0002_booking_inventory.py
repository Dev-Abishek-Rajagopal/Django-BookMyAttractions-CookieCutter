# Generated by Django 3.2.13 on 2022-04-25 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('tickets', models.IntegerField()),
                ('remain_tickets', models.IntegerField()),
                ('rate', models.FloatField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.attraction')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('noftickets', models.IntegerField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.attraction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
