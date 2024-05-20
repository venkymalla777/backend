
from rest_framework import viewsets
from ..models import *
from rest_framework .response import Response
from ..serializers import CommentSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
