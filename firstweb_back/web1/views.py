from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Pizza
from .permissions import IsAdminOrReadOnly
from .serializers import PizzaSerializer


class PizzaAPIList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PizzaAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )