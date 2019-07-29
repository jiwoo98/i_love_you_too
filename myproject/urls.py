from django.contrib import admin
from django.urls import path,include
import myapp.views
import App_account.views
import mypage.views
import App_freeboard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),
    path('post/', myapp.views.post, name = "post"),
    path('account/', include('App_account.urls')),
    path('mypage/', include('mypage.urls')),
    path('freeboard/', include('App_freeboard.urls')),
    path('post_list/', myapp.views.post_list, name = "post_list"),
]