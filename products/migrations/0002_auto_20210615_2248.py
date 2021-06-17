# Generated by Django 3.2.4 on 2021-06-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='static/img/products/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumb',
            field=models.ImageField(blank=True, editable=False, upload_to='static/img/products/'),
        ),
    ]