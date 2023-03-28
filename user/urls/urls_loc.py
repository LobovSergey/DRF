from django.urls import path

from user.views.loc_views import LocationView, LocationDetailView, LocationUpdateView, LocationDeleteView, LocationCreateView

urlpatterns = [
    path('', LocationView.as_view()),
    path('<int:pk>/', LocationDetailView.as_view()),
    path('<int:pk>/update/', LocationUpdateView.as_view()),
    path('<int:pk>/delete/', LocationDeleteView.as_view()),
    path('create/', LocationCreateView.as_view())

]
