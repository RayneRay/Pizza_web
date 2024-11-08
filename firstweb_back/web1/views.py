from rest_framework import generics

from .models import Pizza
from .permissions import IsAdminOrReadOnly
from .serializers import PizzaSerializer


class PizzaAPIList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )

class PizzaAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )

class PizzaAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )