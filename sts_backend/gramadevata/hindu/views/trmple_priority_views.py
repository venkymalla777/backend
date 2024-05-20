from ..serializers import *
from rest_framework import viewsets
from rest_framework .response import Response


class TemplePriorityView(viewsets.ModelViewSet):
    queryset = TemplePriority.objects.all()
    serializer_class = TemplePrioritySerializer

