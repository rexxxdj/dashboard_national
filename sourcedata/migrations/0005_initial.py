# Generated by Django 4.2.17 on 2025-01-06 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sourcedata', '0004_remove_historicaldictionary_category_parrentid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Словник')),
                ('category_parrentId', models.IntegerField(blank=True, null=True, verbose_name='Вища гілка')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
            ],
            options={
                'verbose_name': 'Словник',
                'verbose_name_plural': 'Словники',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDictionary',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Словник')),
                ('category_parrentId', models.IntegerField(blank=True, null=True, verbose_name='Вища гілка')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Додатковий коментар')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Словник',
                'verbose_name_plural': 'historical Словники',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
