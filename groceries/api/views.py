from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import exceptions

from groceries.models import GroceryItem
from groceries.api.serializers import GrocerySerializer


class GroceryViewSet(viewsets.ViewSet):
    def list(self, request):
        # get element block wise
        print("sa")
        print(request.data)
        query = request.data['search']
        print(query)
        queryset = GroceryItem.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))

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

    # def retrieve(self, request, pk=None):
    #     # get one element
    #     if pk > 20:
    #         try:
    #             auth = request.META.get('HTTP_AUTHORIZATION')
    #             print(auth)
    #             _, token = auth.split()
    #             Token.objects.get(key=token)
    #         except:
    #             raise exceptions.AuthenticationFailed('Login Required')
    #     queryset = Element.objects.all()
    #     element_object = get_object_or_404(queryset, atomic_number=pk)
    #     serializer = ElementDetailSerializer(element_object)
    #     return Response(serializer.data)


grocery = GroceryViewSet.as_view({'get': 'list'})
# element = GroceryViewSet.as_view({'get': 'retrieve'})
