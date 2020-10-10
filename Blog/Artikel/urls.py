from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<page>[\d]+)$', ArtikelListView.as_view(), name="list"),
    url(r'^detail/(?P<slug>[\w-]+)/$', ArtikelDetailView.as_view(), name="detail"),
    url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>[\d]+)$', ArtikelKategoriListView.as_view(), name="category"),

]
