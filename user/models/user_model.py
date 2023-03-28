from django.db import models

from user.models.loc_model import Location


class User(models.Model):
    ROLES = [('memder', 'Участник'),
             ('moderator', 'Модератор'),
             ('admin', 'Администратор')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=ROLES, default='member')
    age = models.PositiveIntegerField()
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}({self.role})'
