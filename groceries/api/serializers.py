from rest_framework.serializers import ModelSerializer
from groceries.models import GroceryItem


class GrocerySerializer(ModelSerializer):

    class Meta:
        model = GroceryItem
        fields = ['id', 'title', 'description', 'createdAt', 'price']
