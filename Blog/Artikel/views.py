from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from .models import ArtikelModel
from .forms import ArtikelForm
from django.views.generic import (
    ListView ,
    DetailView,
    CreateView,
    UpdateView ,
    DeleteView
)

class ArtikelDeleteView(DeleteView):
    model               = ArtikelModel
    template_name       = "artikel/artikel_delete_confirmation.html"
    success_url         = reverse_lazy('artikel:manage', kwargs={'page' : 1})
    context_object_name = 'artikel'


class ArtikelUpdateView(UpdateView):
    form_class          = ArtikelForm
    model               = ArtikelModel
    template_name       = "artikel/artikel_update.html"

class ArtikelManageView(ListView):
    model               = ArtikelModel
    template_name       = "artikel/artikel_manage.html"
    context_object_name = 'artikel_list'
    ordering            = ['published']
    paginate_by         = 5


class ArtikelCreateView(CreateView):
    form_class          = ArtikelForm
    template_name       =   "artikel/artikel_create.html"


class ArtikelPerKategori():
    model               = ArtikelModel

    def get_latest_artikel(self):
        kategori_list   = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset        = []

        for kategori in kategori_list:
            artikel     = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel)
        return queryset

class ArtikelListView(ListView):
    model               = ArtikelModel
    template_name       = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering            = ['-published']
    paginate_by         = 3

    def get_context_data(self , *args , **kwargs):
        kategori_list   = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list' : kategori_list})
        kwargs          = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelDetailView(DetailView):
    model               = ArtikelModel
    template_name       = "artikel/artikel_detail.html"
    context_object_name = "artikel"


class ArtikelKategoriListView(ListView):
    model               = ArtikelModel
    template_name       = "artikel/artikel_kategori_list.html"
    context_object_name = 'artikel_list'
    ordering            = ['-published']
    paginate_by         = 3

    def get_queryset(self):
        self.queryset   = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        kategori_list    = self.model.objects.values_list('kategori' , flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list' : kategori_list})
        kwargs           = self.kwargs
        return super().get_context_data(**kwargs)
