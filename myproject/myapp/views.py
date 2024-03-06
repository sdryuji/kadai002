from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from .models import Store


# class StoreSearchListView(ListView):
#     model = Store
#     template_name = 'store_search.html'
#     context_object_name = 'stores'

#     def get_queryset(self):
#         query = self.request.GET.get('query', '')
#         if query:
#             return Store.objects.filter(name__icontains=query)
#         return Store.objects.none()


# class StoreDetailView(DetailView):
#     model = Store
#     template_name = 'store_detail.html'
#     context_object_name = 'store'


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
        {'stores': stores, 'query': query}
    )


def store_detail(request, pk):
    store = Store.objects.get(pk=pk)
    return render(
        request,
        'store_detail.html',
        {
            'store': store,
            })
