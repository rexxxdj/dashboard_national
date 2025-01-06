# Generated by Django 5.1.4 on 2025-01-06 18:23

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категорія майна')),
                ('category_parrentId', models.IntegerField(default=0, verbose_name='Батьківська категорія')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
            ],
            options={
                'verbose_name': 'Категорія майна',
                'verbose_name_plural': 'Категорії майна',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCategory',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категорія майна')),
                ('category_parrentId', models.IntegerField(default=0, verbose_name='Батьківська категорія')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Категорія майна',
                'verbose_name_plural': 'historical Категорії майна',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]