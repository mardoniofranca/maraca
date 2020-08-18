import csv

import os
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django import forms
from .models import Compra, TotalCompra
from .forms import CompraForm, TotalCompraForm
from django.db.models import Sum, Count

from rest_framework import generics
from .serializers import CompraSerializer

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CompraList(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


def login(request):
    return render(request, "login.html")

@login_required(login_url='/accounts/login/')
def index(request):
    total    = TotalCompra.objects.all().values()
    print(total)
    return render(request, 'adm.html', {'total': total})

@login_required(login_url='/accounts/login/')
def compra_pesquisar(request):
    if request.method == "POST":
        compra      = request.POST['compra']
        processo    = request.POST['processo']

        posts       =  Compra.objects.all()
        if (compra != ''):
            posts    = Cliente.objects.filter(compra = compra).all()
        if (processo != ''):
            posts    = posts.filter(nome__icontains = processo).all()

        page = request.GET.get('page', 1)

        paginator = Paginator(posts, 450)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, "compra/tabela.html", {'posts': posts})

        return redirect('/compra/listar/')
    else:
        form = CompraForm()
        return render(request, "compra/filtrar.html",  {'form': form})


@login_required(login_url='/accounts/login/')
def compra_listar(request):
    posts    = Compra.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "compra/tabela.html", {'posts': posts})
