from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', "Изображение"
        VIDEO = 'video', "Видео"
        DOCUMENT = 'document', "Документ"
        GIF = 'gif', "Гиф"

    file = models.FileField(upload_to='only_medias/',
                            verbose_name="Файл",
                            validators=[FileExtensionValidator(
                                allowed_extensions=['png', 'jpg', 'svg', 'jpeg',
                                                    'mp4', 'avi', 'mkv', 'mov',
                                                    'pdf', 'doc', 'docx',
                                                    'gif']
                            )])
    file_type = models.CharField(max_length=10,
                                 verbose_name="Тип файла",
                                 choices=FileType.choices)

    class Meta:
        verbose_name = "Медиа файл"
        verbose_name_plural = "Медиа файлы"

    def __str__(self):
        return f"Id: {self.id}| Name: {self.file.name.split('/')[-1]}"

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError("Недопустимый тип файла")
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split(".")[-1] not in ['png', 'jpg', 'svg', 'jpeg']:
                raise ValidationError("Недопустимое изображение")
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split(".")[-1] not in ['mp4', 'avi', 'mkv', 'mov']:
                raise ValidationError("Недопустимое видео")
        elif self.file_type == self.FileType.DOCUMENT:
            if self.file.name.split(".")[-1] not in ['pdf', 'doc', 'docx']:
                raise ValidationError("Недопустимый документ")
        elif self.file_type == self.FileType.GIF:
            if self.file.name.split(".")[-1] not in ['gif']:
                raise ValidationError("Недопустимый гиф")


class User(models.Model):
    name = models.CharField(max_length=120, verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Feedback(models.Model):
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    author_id = models.OneToOneField(User, verbose_name="author_id", on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
