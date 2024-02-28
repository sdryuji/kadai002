from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class StoreSearchView(TemplateView):
    template_name = 'store_search.html'

    def post(self, request, *args, **kwargs):
        # 検索処理
        return render(request, self.template_name)


class StoreSearchResultView(TemplateView):
    template_name = 'store_search_result.html'

    def post(self, request, *args, **kwargs):
        # 検索処理
        return render(request, self.template_name)
