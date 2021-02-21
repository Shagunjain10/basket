import math
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import PaginateByMaxMixin

from rest_framework import viewsets, exceptions, generics
from rest_framework.response import Response

from groceries.models import GroceryItem
from groceries.api.serializers import GrocerySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'items'


class GroceryList(generics.ListAPIView):
    queryset = GroceryItem.objects.all()

    def get(self, request):

        queryset = self.get_queryset()
        try:
            query = request.data['search']
            queryset = GroceryItem.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query))
        except:
            queryset = GroceryItem.objects.all()
        # Sorting
        try:
            parameter = request.data['parameter']
            if parameter == 'price':
                try:
                    ordering = request.data['ordering']
                    if ordering == 'descending':
                        queryset = queryset.order_by('-price')
                except:
                    queryset = queryset.order_by('price')
            elif parameter == 'created_at':
                try:
                    ordering = request.data['ordering']
                    if ordering == 'descending':
                        queryset = queryset.order_by('-createdAt')
                except:
                    queryset = queryset.order_by('createdAt')
        except:
            pass
        try:
            request.GET._mutable = True
            total_page = int(request.GET.get("totalpage"))
            print(type(total_page))
            items = len(queryset)
            print(request.GET)
            request.GET['items'] = str(math.ceil(items/total_page))
            print(request.GET)
            request.GET._mutable = False
        except:
            pass
        paginator = StandardResultsSetPagination()
        context = paginator.paginate_queryset(queryset, request)
        serializer = GrocerySerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
