from django import forms
from .models import Compra, TotalCompra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('compra','processo','data_publicacao','valor_estimado')


class TotalCompraForm(forms.ModelForm):
    class Meta:
        model = TotalCompra
        fields = ('valor_min','valor_max','valor_medio')
