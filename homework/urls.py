from django.contrib import admin
from django.urls import path, include

from ads.views import ADSView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', include('ads.urls_ads')),
    path('cat/', include('ads.urls_cat')),
    path('user/', include('user.urls_user')),
    path('location/', include('user.urls_loc')),

]
