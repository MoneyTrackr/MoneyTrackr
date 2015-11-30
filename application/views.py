from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Income
from .models import Expense
from .models import Category
from .models import Account
from django.views.generic.base import RedirectView


# Create your views here.

def income(request):
    income_list = Income.objects.all()
    return render(request, 'income/list.html', {'income_list': income_list})

def income_new(request):
    # try:
        # date = models.DateField()
        # category = models.ForeignKey(Category)
        # amount = models.FloatField()
        # account = models.ForeignKey(Account)
        # notes = models.CharField(max_length=50)
     account_list = Account.objects.all()
     category_list = Category.objects.filter(type="income")


     return render(request, 'income/new.html', {'category_list' : category_list, 'account_list' : account_list})

def income_edit(request, income_id):
    try:
        income_id = int(income_id)
    except ValueError:
        raise Http404()
    return render(request, 'income/edit.html', {'income_id': income_id})

def income_delete(request, income_id):
    try:
        income_id = int(income_id)
        income = Income.objects.filter(id=income_id)
        if income.exists():
            income.delete()
    except ValueError:
        raise Http404()
    return HttpResponseRedirect('/income')


def expense(request):
    expense_list = Expense.objects.all()
    return render(request, 'expense/list.html', {'expense_list': expense_list})

def expense_delete(request, expense_id):
    try:
        expense_id = int(expense_id)
        expense = Expense.objects.filter(id=expense_id)
        if expense.exists():
            expense.delete()
    except ValueError:
        raise Http404()
    return HttpResponseRedirect('/')

def expense_new(request):
    return render(request, 'expense/new.html')


def expense_edit(request):
    return HttpResponse("This is my expense edit page")

def home(request):
    return HttpResponse("This is my home page")