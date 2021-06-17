from django.db import models
from django.utils.timezone import now
from django.core.mail import send_mail
from products.models import Product
from baskets.models import Basket


FROM_EMAIL = 'mail@axis-marketing.ru'
TO_EMAIL = 'marukhelin@gmail.com'


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Корзина", editable=False)
    name = models.CharField(max_length=64, verbose_name="Имя", blank=True)
    phone = models.CharField(max_length=64, verbose_name="Телефон", blank=False)
    email = models.CharField(max_length=64, verbose_name="Почта", blank=True)
    description = models.TextField(max_length=64, verbose_name="Описание", blank=True)
    date = models.DateTimeField(default=now, editable=False, verbose_name=u"Создание заказа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Заказ"
        verbose_name_plural = u"Заказы"

    def save(self, *args, **kwargs):
        if not self.pk:
            total_price = 0
            if self.basket and len(self.basket.products.all()) > 0:
                for product_in_basket in self.basket.products.all():
                    total_price += product_in_basket.quantity*product_in_basket.product.price
                message = '''
                    Создан новый заказ. Зайдите в админ панель, чтобы посмотреть подробности.
                    Общая стоимость: {}
                    Дата создания: {}
                    '''.format(total_price, self.date)
                send_mail(
                    u'Заказ на сайте',
                    message,
                    FROM_EMAIL,
                    [TO_EMAIL],
                    fail_silently=True,
                )
        super().save(*args, **kwargs)


class ProductInOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Товар")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=False, verbose_name="Заказ", related_name="products")
    quantity = models.IntegerField(verbose_name="Количество")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = u"Товар в заказе"
        verbose_name_plural = u"Товары в заказе"


class FormApplication(models.Model):
    service = models.CharField(max_length=64, verbose_name="Услуга", blank=True)
    name = models.CharField(max_length=64, verbose_name="Имя", blank=True)
    phone = models.CharField(max_length=64, verbose_name="Телефон")
    description = models.CharField(max_length=64, verbose_name="Описание", blank=True)
    date = models.DateTimeField(default=now, editable=False, verbose_name=u"Создание заказа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Заявка на обратный звонок"
        verbose_name_plural = u"Заявки на обратный звонок"

    def save(self, *args, **kwargs):
        if not self.pk:
            message = '''
                Поступила заявка на обратный звонок.
                Дата создания: {}
                Имя: {}
                Телефон: {}
                '''.format(self.date, self.name, self.phone)
            if self.service:
                message += '''
                    Услуга: {}
                '''.format(self.service)
            if self.description:
                message += '''
                    Описание: {}
                '''.format(self.description)
            send_mail(
                u'Заявка с сайта',
                message,
                FROM_EMAIL,
                [TO_EMAIL],
                fail_silently=True,
            )
        super().save(*args, **kwargs)


