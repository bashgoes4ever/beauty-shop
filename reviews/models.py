from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class ImageReview(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Имя")
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/reviews/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/reviews/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Фотоотзыв"
        verbose_name_plural = u"Фотоотзывы"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 214, 343):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)


class VideoReview(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Имя")
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/reviews/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/reviews/')
    video_url = models.CharField(max_length=64, blank=False, null=False, verbose_name="Ссылка на видео")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Видеоотзыв"
        verbose_name_plural = u"Видеоотзывы"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 573, 320):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)
