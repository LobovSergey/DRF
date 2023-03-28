from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView, ListAPIView

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


class AnnouncementDetailView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementCreateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementUpdateView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementDeleteView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDeleteSerializer

# @method_decorator(csrf_exempt, name="dispatch")
# class AnnouncementUploadImageView(UpdateView):
#     model = Announcement
#     fields = ['image']
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.image = request.FILES['image']
#         self.object.save()
#         return JsonResponse(
#             {
#                 "image": self.object.image.url if self.object.image else None
#             }
#         )
