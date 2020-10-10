from django.db import models
from django.utils.text import slugify

class ArtikelModel(models.Model):
    judul           = models.CharField(max_length=100)
    isi             = models.TextField()
    kategori        = models.CharField(max_length=255)
    published       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(blank=True , editable=False)

    def save(self, **kwargs):
        self.slug = slugify(self.judul)
        return super().save(**kwargs)

    def __str__(self):
        return "{} - {}".format(self.id, self.judul)
