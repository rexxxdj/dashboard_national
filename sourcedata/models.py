import datetime
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


# Create your models here.
class EquipmentCategory(models.Model):
	name = models.CharField(max_length=50,
							blank=False, 
							null=False, 
							verbose_name='Назва')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Категорія'
		verbose_name_plural = 'Майно. Категорії'

	def get_update_url(self):
		return reverse('directory_equipment_category_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipment_category_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.



class EquipmentStatus(models.Model):
	name = models.CharField(max_length=50,
							blank=False, 
							null=False, 
							verbose_name='Назва')
	notes = models.CharField(max_length=200,
							blank=True, 
							null=True, 
							verbose_name='Додатковий коментар')
	history = HistoricalRecords()

	class Meta:
		verbose_name = 'Статус'
		verbose_name_plural = 'Майно. Статуси'

	def get_update_url(self):
		return reverse('directory_equipment_status_update',
			args=[self.id])

	def get_delete_url(self):
		return reverse('directory_equipment_ststus_delete',
			args=[self.id])

	def __str__(self):
		return self.name # Наприклад - Ноутбук, Планшет, ПК, Радіостанція, Серверна шафа і т.д.