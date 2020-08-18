from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
admin.autodiscover()
import posts.views
from posts.views import CompraList

urlpatterns = [
    url(r'^comprarest/$', posts.views.CompraList.as_view(), name='compra-list'),

    path('admin/', admin.site.urls),
    path('accounts/'    ,       include('django.contrib.auth.urls')),
    path(""             ,       posts.views.index, name="index"),
    path("compra/listar_compras/",               posts.views.compra_listar,   name="compra_listar"),

]
