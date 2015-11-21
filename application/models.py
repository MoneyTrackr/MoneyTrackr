from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)

class Account(models.Model):
    name = models.CharField(max_length=30)

class Income(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category)
    amount = models.FloatField()
    account = models.ForeignKey(Account)
    notes = models.CharField(max_length=50)

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category)
    amount = models.FloatField()
    account = models.ForeignKey(Account)
    notes = models.CharField(max_length=50)

