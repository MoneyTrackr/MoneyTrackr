from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def income(request):
    return HttpResponse("This is my income page")

def income_new(request):
    return HttpResponse("This is my income new page")

def income_edit(request, income_id):
    try:
        income_id = int(income_id)
    except ValueError:
        raise Http404()
    html = "<html><body>This is my income edit page for income entry no. %s.</body></html>" % (income_id)
    return HttpResponse(html)

def expense(request):
    return HttpResponse("This is my expense page")

def expense_new(request):
    return HttpResponse("This is my expense new page")

def expense_edit(request):
    return HttpResponse("This is my expense edit page")

def home(request):
    return HttpResponse("This is my home page")