from django.db import models

from ads.models.cat_model import Category
from user.models.user_model import User


class Announcement(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(null=True, default=False)
    image = models.ImageField(upload_to='pic/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-price']

    def __str__(self):
        return f'{self.category}/{self.name} - {self.price}'
