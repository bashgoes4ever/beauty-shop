from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from django.core.paginator import Paginator


class ProductCategories(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        objs = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(objs, many=True)
        return Response(serializer.data)


class Products(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category_id):
        objs = Product.objects.filter(category=category_id) # .order_by("-priority")

        paginator = Paginator(objs, 10)
        page_num = request.GET.get('page', 1)
        paginated_objs = paginator.get_page(page_num)

        serializer = ProductSerializer(paginated_objs, many=True)
        next_page = paginated_objs.next_page_number() if paginated_objs.has_next() else -1
        return Response({
            'data': serializer.data,
            'next_page': next_page
        })


class ProductsHome(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        objs = Product.objects.filter(is_main_page=True).order_by("-priority")
        serializer = ProductSerializer(objs, many=True)
        return Response(serializer.data)

