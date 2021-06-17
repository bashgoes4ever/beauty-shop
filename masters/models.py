from django.db import models
from base.models import ModelWithCategory
from utils.make_thumbnail import make_thumbnail


class Master(ModelWithCategory):
    name = models.CharField(max_length=64, blank=False, null=False, verbose_name="Имя")
    job = models.CharField(max_length=64, blank=False, null=False, verbose_name="Должность")
    image = models.ImageField(verbose_name="Изображение", upload_to='static/img/masters/')
    thumb = models.ImageField(blank=True, editable=False, upload_to='static/img/masters/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Мастер"
        verbose_name_plural = u"Наши мастера"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.thumb, 374, 523):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super().save(*args, **kwargs)


class MasterSkill(models.Model):
    master = models.ForeignKey(Master, blank=False, null=False, related_name='skills',
                                    on_delete=models.CASCADE, verbose_name=u"Мастер")
    skill = models.CharField(max_length=64, blank=False, null=False, verbose_name="Умение")
