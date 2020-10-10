from django.conf.urls import url , include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='blog/index.html'), name='home'),
    url(r'^artikel/', include('Artikel.urls', namespace='artikel')),
]
