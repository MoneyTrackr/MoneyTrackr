from django import forms
from .models import Income
from .models import Account
from .models import Category
from django.core import serializers

class NewIncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('date', 'category','amount', 'account','notes')
        