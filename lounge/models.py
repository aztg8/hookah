from django.db import models
from common.models import Media


class Metro(models.Model):
    title = models.CharField(max_length=120, verbose_name="Станция метро")

    def __str__(self):
        return self.title


class Lounge(models.Model):
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE,
                              verbose_name="Метро")
    title = models.CharField(max_length=120, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    phone = models.CharField(max_length=120, verbose_name="Номер телефона")
    work_time = models.CharField(max_length=120, verbose_name="Время работы")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title


class Address(models.Model):
    lounge_id = models.ForeignKey(Lounge, verbose_name="Lounge ID", on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Название")
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.title


class LoungePhoto(models.Model):
    photo = models.ForeignKey(Media, verbose_name="Фото", on_delete=models.CASCADE)
    lounge = models.ForeignKey(Lounge, verbose_name="Lounge", on_delete=models.CASCADE)

    def __str__(self):
        return self.lounge
