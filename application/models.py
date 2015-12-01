from django.db import models
from django.core import serializers

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Income(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category)
    amount = models.FloatField()
    account = models.ForeignKey(Account)
    notes = models.CharField(max_length=50)
    # account_list = Account.objects.all()
    # category_list = Category.objects.filter(type="income")
    # cat_data = serializers.serialize('python', category_list, fields=('id','name'))
    # acc_data = serializers.serialize('python', account_list, fields=('id','name'))
    # category = models.CharField(max_length=1, choices=cat_data)


class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category)
    amount = models.FloatField()
    account = models.ForeignKey(Account)
    notes = models.CharField(max_length=50)