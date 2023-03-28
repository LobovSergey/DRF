from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models.cat_model import Category
from ads.serializers.cat_serializer import CategorySerializer, CategoryDetailSerializer, CategoryCreateSerializer, \
    CategoryUpdateSerializer, CategoryDeleteSerializer


class ADSView(View):

    @staticmethod
    def get(request):
        from django.http import JsonResponse
        return JsonResponse({"status": "ok"}, status=200)


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
