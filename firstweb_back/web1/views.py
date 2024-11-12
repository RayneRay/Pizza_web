import json

from django.http import HttpResponse
from rest_framework import generics

from .models import Pizza
from .permissions import IsAdminOrReadOnly
from .serializers import PizzaSerializer


class PizzaAPIList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def post(self, request, *args, **kwargs):
        file = request.data['C:\PythonProjects\Website_Pizza\picture']
        preview = Pizza.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

class PizzaAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )

class PizzaAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = (IsAdminOrReadOnly, )