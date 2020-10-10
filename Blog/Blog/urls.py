from django.conf.urls import url , include
from django.contrib import admin
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BlogHomeView.as_view() , name='home'),
    url(r'^artikel/', include('Artikel.urls', namespace='artikel')),
]
