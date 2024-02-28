from django.shortcuts import render
from django.views.generic import TemplateView
from myapp.models import StoreDetail


class SearchResultView(TemplateView):
    template_name = 'search_result.html'

    def post(self, request, *args, **kwargs):
        # 検索処理
        return render(request, self.template_name)


class SearchView(TemplateView):
    template_name = 'search.html'

    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query', '')
        hit_store_detail = StoreDetail.objects.filter(name__icontains=search_query)
        context = {
            # キー名がhtmlに渡される
            'hit_store_detail': hit_store_detail,
            'search_query': search_query,
        }
        return render(request, 'result.html', context)
