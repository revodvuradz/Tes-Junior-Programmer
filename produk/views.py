from django.shortcuts import render, get_object_or_404, redirect
from .models import Produk, Status, Kategori
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.contrib import messages


def produk_list(request):
    produk_list = Produk.objects.filter(status__nama_status="bisa dijual")

    search = request.GET.get('search')
    if search:
        produk_list = produk_list.filter(nama_produk__icontains=search)

    paginator = Paginator(produk_list, 10)  # 🔥 10 produk per halaman
    page_number = request.GET.get('page')
    produk = paginator.get_page(page_number)

    return render(request, 'produk/produk_list.html', {
        'produk': produk,
    })

def produk_create(request):
    from .forms import ProdukForm
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil ditambahkan")
        return redirect('produk_list')
    return render(request, 'produk/produk_form.html', {'form': form})

def produk_update(request, pk):
    from .forms import ProdukForm
    produk = get_object_or_404(Produk, pk=pk)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect('produk_list')
    return render(request, 'produk/produk_form.html', {'form': form})

@require_POST
def produk_bulk_delete(request):
    ids = request.POST.getlist('produk_ids')
    if ids:
        Produk.objects.filter(pk__in=ids).delete()
        messages.success(request, "Produk berhasil dihapus!")
    return redirect('produk_list')

