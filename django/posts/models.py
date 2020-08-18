from django.db import models
from django.urls import reverse
from django.utils import timezone

class Compra(models.Model):
    codigo          = models.AutoField(primary_key=True)
    compra          = models.CharField(max_length=250, default ="Nome")
    processo        = models.CharField(max_length=250, default ="Lideranca")
    data_publicacao = models.DateTimeField(default=timezone.now,blank=True)
    valor_estimado  = models.FloatField(default=0,blank=True)
    valor_min       = models.FloatField(default=0,blank=True)
    valor_medio     = models.FloatField(default=0,blank=True)
    valor_max       = models.FloatField(default=0,blank=True)

    def __str__(self):
        return "%s | %s | %s | %s | %s | %s " % (self.compra, self.processo, self.data_publicacao, self.valor_estimado)


class TotalCompra(models.Model):
    codigo          = models.AutoField(primary_key=True)
    valor_min       = models.FloatField(default=0,blank=True)
    valor_medio     = models.FloatField(default=0,blank=True)
    valor_max       = models.FloatField(default=0,blank=True)
    valor           = models.FloatField(default=0,blank=True)

    def __str__(self):
        return "%s | %s | %s " % (self.valor_min, self.valor_medio, self.valor_max)

class Fornecedor(models.Model):
    codigo          = models.AutoField(primary_key=True)
    cnpj            = models.CharField(max_length=250, default ="Nome")
    valor           = models.FloatField(default=0,blank=True)

    def __str__(self):
        return "%s | %s | %s " % (self.codigo, self.cnpj, self.valor)
