from django.db.models import Q
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView

from ads.serializers.ads_serializer import AnnouncementSerializer, AnnouncementDetailSerializer, \
    AnnouncementCreateSerializer, \
    AnnouncementUpdateSerializer, AnnouncementDeleteSerializer
from ads.models.ads_model import Announcement


class ADSView(View):

    @staticmethod
    def get(request):
        return JsonResponse({"status": "ok"}, status=200)


class AnnouncementView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        querry_args = request.query_params

        if querry_args['text']:
            self.queryset = self.queryset.filter(description__icontains=querry_args['text'])
        if querry_args['category_id']:
            self.queryset = self.queryset.filter(category_id=querry_args['category_id'])
        if querry_args['price_from'] and querry_args['price_to']:
            self.queryset = self.queryset.filter(price__range=[querry_args['price_from'], querry_args['price_to']])
        if querry_args['price_from']:
            self.queryset = self.queryset.filter(price__gte=querry_args['price_from'])
        if querry_args['price_to']:
            self.queryset = self.queryset.filter(price__lte=querry_args['price_to'])

        return super().get(request, *args, **kwargs)


class AnnouncementDetailView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementCreateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementUpdateView(RetrieveUpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementDeleteView(RetrieveDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDeleteSerializer


class AnnouncementImageView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer
