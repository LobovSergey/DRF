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
        q = request.query_params
        print(q)
        searched_text = request.query_params.get('text', None)
        searched_cat_id = request.query_params.get('category_id', None)
        price_from = request.query_params.get('price_from', None)
        price_to = request.query_params.get('price_to', None)

        if searched_text:
            self.queryset = self.queryset.filter(description__icontains=searched_text)
        if searched_cat_id:
            self.queryset = self.queryset.filter(category_id=searched_cat_id)
        if price_from and price_to:
            self.queryset = self.queryset.filter(price__range=[price_from, price_to])
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

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
