from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from user.models.user_model import Location
from user.serializers.loc_serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        searched_loc = request.query_params.get('location', None)

        if searched_loc:
            self.queryset = self.queryset.filter(user__location__name__icontains=searched_loc)

        return super().get(request, *args, **kwargs)
