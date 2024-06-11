from django.db import models
from tobacco.models import Product


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название тэга")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class Variants(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название варианта")

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

    def __str__(self):
        return self.title


class Mix(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название микса")
    desc = models.TextField(verbose_name="Описание")
    tag = models.ManyToManyField(Tag)
    variants = models.ManyToManyField(Variants)
    category_id = models.IntegerField(verbose_name='ID категории')

    def __str__(self):
        return self.title


class MixPart(models.Model):
    mix_id = models.ForeignKey(Mix, on_delete=models.CASCADE,
                               verbose_name='ID микса')
    tobacco_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   verbose_name='ID табака')
    percentage = models.IntegerField(verbose_name='Процент')
