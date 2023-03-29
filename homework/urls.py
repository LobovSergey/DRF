from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views.ads_views import ADSView, AnnouncementImageView
from user.views.loc_views import LocationViewSet, LocationView

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', include('ads.urls.urls_ads')),
    path('cat/', include('ads.urls.urls_cat')),
    path('user/', include('user.urls.urls_user')),
    path('location/', LocationView.as_view()),
    path('media/pic/<int:pk>', AnnouncementImageView.as_view())

]

urlpatterns += router.urls
