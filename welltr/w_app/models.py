from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=155, blank=True, null=True, verbose_name='имя')
   

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователя'

    def __str__(self):
        return str(self.name)


class Data(models.Model):
    steps = models.IntegerField(default=0, blank=True, null=True, verbose_name='количество шагов')
    date = models.DateField(default=timezone.now, verbose_name='время')
    user = models.ForeignKey(User, related_name='data', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Данные')

    class Meta:
        verbose_name='Данные'
        verbose_name_plural='Данные'

    def __str__(self):
        return str(self.user)
