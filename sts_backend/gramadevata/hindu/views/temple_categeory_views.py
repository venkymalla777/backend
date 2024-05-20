from ..serializers import *
from rest_framework import viewsets

from rest_framework .response import Response
from django.db.models import Q




class templeCategeoryview(viewsets.ModelViewSet):
    queryset = TempleCategory.objects.all()
    serializer_class = TempleCategeorySerializer

