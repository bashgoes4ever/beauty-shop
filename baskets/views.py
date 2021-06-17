from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework import status


class BasketView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        try:
            # if 'HTTP_AUTHORIZATION' not in request.META:
            #     request.session.create()
            #     session_key = request.session.session_key
            # else:
            #     session_key = request.META['HTTP_AUTHORIZATION']
            if not request.session.exists(request.session.session_key):
                request.session.create()
            session_key = request.session.session_key
            obj, created = Basket.objects.get_or_create(user=session_key)
            serializer = BasketSerializer(obj)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductInBasketView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, product_id):
        try:
            basket, created = Basket.objects.get_or_create(user=request.session.session_key)
            serializer = ProductInBasketCreateSerializer(data={
                "basket": basket.id,
                "product": product_id,
                "quantity": 1
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        try:
            product = ProductInBasket.objects.get(id=product_id)
            serializer = ProductInBasketUpdateSerializer(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.update(product, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        try:
            product = ProductInBasket.objects.get(id=product_id)
            product.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

