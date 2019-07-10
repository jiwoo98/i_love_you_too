from django.contrib import admin
from django.urls import path,include
import myapp.views
import App_account.views
import mypage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('post/', myapp.views.post, name = "post"),
    path('account/', include('App_account.urls')),
    path('mypage/', include('mypage.urls')),
]
