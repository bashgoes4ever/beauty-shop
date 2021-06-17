from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория товаров"
        verbose_name_plural = u"Категории товаров"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, blank=False, null=False, related_name='products',
                                 on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Название")
    text = models.TextField(max_length=256, blank=False, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/products/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/products/')
    priority = models.IntegerField(verbose_name="Приоритет")
    is_main_page = models.BooleanField(verbose_name="Выводить на главной", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Товар"
        verbose_name_plural = u"Товары"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 358, 273):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)
