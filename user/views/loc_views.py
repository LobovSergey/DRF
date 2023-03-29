from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from user.models.user_model import Location
from user.serializers.loc_serializers import LocationSerializer, LocationDetailSerializer, LocationCreateSerializer, \
    LocationUpdateSerializer, LocationDeleteSerializer


class LocationView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        searched_loc = request.query_params.get('location', None)

        if searched_loc:
            self.queryset = self.queryset.filter(user__location__name__icontains=searched_loc)

        return super().get(request, *args, **kwargs)


class LocationDetailView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationCreateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class LocationUpdateView(UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class LocationDeleteView(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDeleteSerializer
