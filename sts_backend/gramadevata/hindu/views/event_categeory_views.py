from rest_framework import viewsets
from ..models import *
from ..serializers import EventCategorySerializer

class EventCategoryView(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
