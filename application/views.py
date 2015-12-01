from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Income
from .models import Expense
from .models import Category
from .models import Account
from .forms import NewIncomeForm
from .forms import NewExpenseForm
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# Create your views here.

def income(request):
    income_list = Income.objects.all()
    return render(request, 'income/list.html', {'income_list': income_list})

def income_new(request):
    post = Income()

    if request.method == "POST":
        form = NewIncomeForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return HttpResponseRedirect('/income')
    else:
        form = NewIncomeForm()
    return render(request, 'income/new.html', {'form': form})

def income_edit(request, income_id):
    income_id = int(income_id)
    post = get_object_or_404(Income,id=income_id)
    
    if request.method == "POST":
        form = NewIncomeForm(request.POST, instance=post)
        if form.is_valid():
            #post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/income')
    else:
        form = NewIncomeForm(instance=post)
    return render(request, 'income/edit.html', {'form': form})
    
    #try:
    #    income_id = int(income_id)
    #except ValueError:
    #    raise Http404()
    #return render(request, 'income/edit.html', {'income_id': income_id})

def income_delete(request, income_id):
    try:
        income_id = int(income_id)
        income = Income.objects.filter(id=income_id)
        if income.exists():
            income.delete()
    except ValueError:
        raise Http404()
    return HttpResponseRedirect('/income')

#create new method for add_expense_link

def expense(request):
    expense_list = Expense.objects.all()
    return render(request, 'expense/list.html', {'expense_list': expense_list})

def expense_new(request):
    post = Expense()

    if request.method == "POST":
        form = NewExpenseForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return HttpResponseRedirect('/expense')
    else:
        form = NewExpenseForm()
    return render(request, 'expense/new.html', {'form': form})

def expense_edit(request, expense_id):
    try:
        expense_id = int(expense_id)
        expense = Expense.objects.get(id=expense_id)
    except ValueError:
        raise Http404()
    return render(request, 'expense/edit.html', {'expense': expense})

def expense_delete(request, expense_id):
    try:
        expense_id = int(expense_id)
        expense = Expense.objects.filter(id=expense_id)
        if expense.exists():
            expense.delete()
    except ValueError:
        raise Http404()
    return HttpResponseRedirect('/')

def home(request):
    return HttpResponse("This is my home page")
