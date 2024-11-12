from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    preview = models.ImageField(max_length=None)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} {self.price}'