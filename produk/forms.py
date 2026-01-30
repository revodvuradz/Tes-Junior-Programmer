from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama produk'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan harga'
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

