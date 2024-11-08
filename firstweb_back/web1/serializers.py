from email.policy import default

from rest_framework import serializers
from web1.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pizza
        fields = ('name', 'description', 'price', 'user')
