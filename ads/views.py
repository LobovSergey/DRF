import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count

from django.http import JsonResponse
from django.shortcuts import get_list_or_404

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Announcement, Category


class ADSView(View):

    @staticmethod
    def get(request):
        return JsonResponse({"status": "ok"}, status=200)


class AnnouncementView(ListView):
    model = Announcement

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_data = request.GET.get('price', None)
        if search_data:
            self.object_list = get_list_or_404(self.object_list, price=search_data)

        self.object_list = self.object_list.select_related("author")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        data_announcement = [
            {
                'id': announcement.id,
                'name': announcement.name,
                'description': announcement.description,
                'price': announcement.price,
                'author_id': announcement.author_id,
                'category_id': announcement.category_id

            } for announcement in page_object
        ]

        result = {
            "items": data_announcement,
            'total_ads': Announcement.objects.filter(is_published=True).aggregate(Count('is_published'))[
                "is_published__count"],
            "total": paginator.count,
            "num_pages": paginator.num_pages
        }

        return JsonResponse(result, safe=False)


class AnnouncementDetailView(DetailView):
    model = Announcement

    def get(self, request, *args, **kwargs):
        try:
            announcement = self.get_object()
            return JsonResponse(
                {
                    'id': announcement.id,
                    'name': announcement.name,
                    'description': announcement.description,
                    'price': announcement.price,
                    'author_id': announcement.author_id,
                    'category_id': announcement.category_id,

                }, status=200)

        except Exception:
            return JsonResponse({"error": "Not found"}, safe=False, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['name', 'price', 'description', 'author', 'category']

    def post(self, request, *args, **kwargs):
        announcement_data = json.loads(request.body)
        announcement = Announcement.objects.create(
            name=announcement_data["name"],
            price=announcement_data["price"],
            description=announcement_data["description"],
            author_id=announcement_data["author_id"],
            category_id=announcement_data["category_id"]
        )
        return JsonResponse({"status": "created",
                             "id": announcement.id,
                             "name": announcement.name,
                             "description": announcement.description}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['name', 'price', 'description']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        announcement_data = json.loads(request.body)
        self.object.name = announcement_data["name"]
        self.object.description = announcement_data["description"]
        self.object.price = announcement_data["price"]
        self.object.author_id = announcement_data["author_id"]
        self.object.category_id = announcement_data["category_id"]
        self.object.save()
        return JsonResponse({"status": "edited",
                             "id": self.object.id,
                             "name": self.object.name,
                             "description": self.object.description,
                             "author_id": self.object.author_id,
                             "category_id": self.object.category_id}, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {
                "status": "deleted"
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementUploadImageView(UpdateView):
    model = Announcement
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES['image']
        self.object.save()
        return JsonResponse(
            {
                "image": self.object.image.url if self.object.image else None
            }
        )


class CategoriesView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_data = request.GET.get('name', None)
        if search_data:
            self.object_list = self.object_list.filter(price=search_data)
        result = [
            {
                'id': category.id,
                'name': category.name
            } for category in self.object_list
        ]
        return JsonResponse(result, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
            return JsonResponse(
                {
                    "id": category.id,
                    "name": category.name,
                }, status=200)
        except Exception:
            return JsonResponse({"error": "Not found"}, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        announcement = Category.objects.create(
            name=cat_data["name"]
        )
        return JsonResponse({
            "status": "created",
            "id": announcement.id,
            "name": announcement.name
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]
        self.object.save()
        return JsonResponse({
            "status": "edited",
            "id": self.object.id,
            "name": self.object.name
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {
                "status": "deleted"
            }
        )
