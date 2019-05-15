# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#comando python manage.py inspectdb > mortalidade/models.py

class Country(models.Model):
    class Meta:
        db_table= "country"

    iso_code =models.CharField(primary_key=True,max_length=20)  # This field type is a guess.
    country_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
    	return self.country_name
    


class Mortality(models.Model):
    class Meta:
        db_table= "mortality"

    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='iso_code')  # This field type is a guess.
    median = models.TextField(blank=True, null=True)  # This field type is a guess.
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    
