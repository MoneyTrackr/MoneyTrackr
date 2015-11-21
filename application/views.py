from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Income
from .models import Expense


# Create your views here.

def income(request):
    income_list = Income.objects.all()
    return render(request, 'income/list.html', {'income_list': income_list})

def income_new(request):
    return HttpResponse("This is my income new page")

def income_edit(request, income_id):
    try:
        income_id = int(income_id)
    except ValueError:
        raise Http404()
    return render(request, 'income/edit.html', {'income_id': income_id})

def expense(request):
    expense_list = Expense.objects.all()
    return render(request, 'expense/list.html', {'expense_list': expense_list})


def expense_new(request):
    return render(request, 'expense/new.html')


def expense_edit(request):
    return HttpResponse("This is my expense edit page")

def home(request):
    return HttpResponse("This is my home page")