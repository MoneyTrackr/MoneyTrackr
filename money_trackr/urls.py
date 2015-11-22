"""money_trackr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from application.views import income, expense, home, income_new, income_edit, expense_delete, expense_new, expense_edit
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^income/$', income),
    url(r'^income/new$', income_new),
    url(r'^income/(\d+)/edit$', income_edit),
    url(r'^expense/(\d+)/delete', expense_delete),
    url(r'^expense/$', expense),
    url(r'^expense/new$', expense_new),
    url(r'^expense/\d+/edit$', expense_edit),
    url(r'^$', RedirectView.as_view(url='/expense', permanent=False)),
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)