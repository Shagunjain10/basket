from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import exceptions

from groceries.models import GroceryItem
from groceries.api.serializers import GrocerySerializer


class GroceryViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            print(request.data)
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
        serializer = GrocerySerializer(queryset, many=True)
        return Response(serializer.data)


grocery = GroceryViewSet.as_view({'get': 'list'})
