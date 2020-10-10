from django import forms
from django.forms import ModelForm
from .models import ArtikelModel

class ArtikelForm(ModelForm):
    class Meta:
        model       = ArtikelModel
        fields      = [
            'judul' , 'isi', 'kategori'
        ]
        widgets     = {
            'judul' : forms.TextInput(
                attrs = {
                    'class' :'form-control',
                    'placeholder' : 'Masukan Judul Artikel Disini'
                }
            ),

            'isi'   : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Isi Artikel Disini'
                }
            ),

            'kategori' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Masukan Kategori Artikel Disini'
                }
            )
        }
