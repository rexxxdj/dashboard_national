# Generated by Django 4.2.17 on 2025-01-06 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sourcedata', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Майно. Статуси',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEquipmentStatus',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Статус',
                'verbose_name_plural': 'historical Майно. Статуси',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]