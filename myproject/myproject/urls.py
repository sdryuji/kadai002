from django.contrib import admin
from django.urls import path
# Include関数をインポート
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

# path関数でApp_Folder内のurls.pyを読み込むために、include関数を記述
urlpatterns = [
    path('admin/', admin.site.urls),          # 管理画面のPath
    path("", views.TopView.as_view(), name="top"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', include('django.contrib.auth.urls')),
    path('myapp/', include('myapp.urls')),    # アプリケーション管理フォルダのurls.pyと関連づけるpath
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
