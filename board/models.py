from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.name}'


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo: автодобавление даты, переделать миграции
    # create_ts = models.DateTimeField(auto_now_add=True)
    create_ts = models.DateTimeField()
    title = models.CharField(max_length=400)
    content = models.TextField(blank=True, null=True, verbose_name='text')
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        date_str = datetime.strftime(self.create_ts, '%d.%m.%y %H:%M')
        title_short = self.title if len(self.title) <= 30 else self.title[:30] + '…'
        return f'{date_str} {self.user} {title_short}'


class Reply(models.Model):
    class Meta:
        verbose_name_plural = 'replies'

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # todo: автодобавление даты, переделать миграции
    # create_ts = models.DateTimeField(auto_now_add=True)
    create_ts = models.DateTimeField()
    content = models.TextField(verbose_name='text')
    accepted = models.BooleanField()

    def __str__(self):
        date_str = datetime.strftime(self.create_ts, '%d.%m.%y %H:%M')
        return f'{date_str} {self.user} to {self.ad}'
