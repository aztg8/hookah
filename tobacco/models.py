from django.db import models
from common.models import Media


class Manufacturer(models.Model):
    title = models.CharField(max_length=120, verbose_name="Производитель")

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название тэга")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=120, verbose_name="Название страны")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.title


class PrepMethod(models.Model):
    title = models.CharField(max_length=120, verbose_name="Метод приготовления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Метод приготовления"
        verbose_name_plural = "Методы приготовления"


class Product(models.Model):
    class StrengthType(models.TextChoices):
        first = "strong", 'крепкий'

    title = models.CharField(max_length=120, verbose_name="Название продукта")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,
                                     verbose_name="Производитель")
    leaf = models.CharField(max_length=120, verbose_name="Из какого листа")
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                verbose_name="Страна")
    composition = models.CharField(max_length=120, verbose_name="Состав")
    strength = models.CharField(max_length=120, verbose_name="Крепость", choices=StrengthType.choices)
    taste = models.CharField(max_length=120, verbose_name="Вкус")
    type = models.CharField(max_length=120, verbose_name="Тип")
    photo = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name="Фото")
    tag = models.ManyToManyField(Tag, verbose_name="Тэг")
    preparation = models.ManyToManyField(PrepMethod)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
