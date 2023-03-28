from django.contrib import admin
from django.urls import path, include

from ads.views.ads_views import ADSView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', include('ads.urls.urls_ads')),
    path('cat/', include('ads.urls.urls_cat')),
    path('user/', include('user.urls.urls_user')),
    path('location/', include('user.urls.urls_loc')),

]
