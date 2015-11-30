from django import forms
from .models import Income
from .models import Account
from .models import Category
from django.core import serializers

class NewIncomeForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.filter(type="income"), empty_label=" ")
	account = forms.ModelChoiceField(queryset=Account.objects.only(), empty_label=" ")

	class Meta:
		model = Income
		fields = ('date', 'category','amount', 'account','notes')