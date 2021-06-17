from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class Brand(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False)
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/brands/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/brands/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Бренд"
        verbose_name_plural = u"Бренды"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 140, 120):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)


