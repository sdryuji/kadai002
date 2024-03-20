from django.shortcuts import render
from .models import Store
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class TopView(TemplateView):
    template_name = 'top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


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
