from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm
from django.contrib.auth.views \
    import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm  # 作成した登録用フォームを設定
    template_name = "myapp/signup.html"
    success_url = reverse_lazy("myapp:index")  # ユーザー作成後のリダイレクト先ページ

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response


# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "myapp/login.html"


# LogoutViewを追加
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("myapp:index")


class TopView(TemplateView):
    template_name = 'top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ctx['title'] = 'test'
        return ctx
