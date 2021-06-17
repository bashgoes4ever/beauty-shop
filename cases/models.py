from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class Case(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False)
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/cases/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/cases/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Кейс"
        verbose_name_plural = u"Наши работы"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 382, 488):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)


