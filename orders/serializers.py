from rest_framework import serializers
from .models import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormApplication
        fields = '__all__'

    def create(self, validated_data):
        application = FormApplication.objects.create(**validated_data)
        return application


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        session_key = self.context['request'].session.session_key
        basket, created = Basket.objects.get_or_create(user=session_key)
        order, created = Order.objects.get_or_create(basket=basket, **validated_data)
        if len(basket.products.all()):
            for product_in_basket in basket.products.all():
                ProductInOrder.objects.create(
                    product=product_in_basket.product,
                    order=order,
                    quantity=product_in_basket.quantity,
                    price=product_in_basket.product.price
                )
        return order
