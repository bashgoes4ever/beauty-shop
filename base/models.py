from django.db import models


CATEGORIES = (
    ('haircuts', 'Парикмахерские услуги'),
    ('nails', 'Маникюр'),
    ('eyebrows', 'Брови')
)


class ModelWithCategory(models.Model):
    category = models.CharField(max_length=32, choices=CATEGORIES, default='haircuts')
