from Artikel.models import ArtikelModel
from Artikel.views import ArtikelPerKategori
from django.views.generic import TemplateView

class BlogHomeView(TemplateView, ArtikelPerKategori):
    template_name       = "blog/index.html"


    def get_context_data(self):
        querysets   = self.get_latest_artikel()
        context     = {
         'latest_artikel_list' : querysets
        }
        return context
