from django.shortcuts import render
from .models import Store


def store_list(request):
    stores = Store.objects.all()
    query = request.GET.get('q', '')
    if query:
        stores = stores.filter(name__icontains=query) | \
                 stores.filter(address__icontains=query) | \
                 stores.filter(genre__icontains=query) | \
                 stores.filter(prefecture__icontains=query)
    return render(
        request,
        'store_list.html',
        {
            'stores': stores,
            'query': query
        }
    )


def store_detail(request, pk):
    store = Store.objects.get(pk=pk)
    return render(
        request,
        'store_detail.html',
        {
            'store': store,
        }
    )
