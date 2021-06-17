from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class ServiceCategory(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Название")
    description = models.TextField(max_length=256, blank=False, null=False, verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/services/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/services/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория услуг"
        verbose_name_plural = u"Категории услуг"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 374, 552):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, blank=False, null=False, related_name='services',
                                 on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"
