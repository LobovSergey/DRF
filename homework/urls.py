from django.contrib import admin
from django.urls import path, include

from ads.views.ads_views import ADSView, AnnouncementImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', include('ads.urls.urls_ads')),
    path('cat/', include('ads.urls.urls_cat')),
    path('user/', include('user.urls.urls_user')),
    path('location/', include('user.urls.urls_loc')),
    path('media/pic/<int:pk>', AnnouncementImageView.as_view())

]
