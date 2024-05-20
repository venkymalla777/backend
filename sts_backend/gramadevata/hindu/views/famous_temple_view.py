
from sqlalchemy import create_engine
from rest_framework import generics
from ..models import Temple, FamousTemple
from ..serializers import TempleSerializer, FamousTempleSerializer
from rest_framework import viewsets

class FamousTempleListCreateView(viewsets.ModelViewSet):
    queryset = FamousTemple.objects.all()
    serializer_class = FamousTempleSerializer