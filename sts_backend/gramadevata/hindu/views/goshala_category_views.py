from rest_framework import viewsets
from ..models import GoshalaCategory
from ..serializers import GoshalaCategorySerializer

class GoshalaCategoryViewSet(viewsets.ModelViewSet):
    queryset = GoshalaCategory.objects.all()
    serializer_class = GoshalaCategorySerializer
