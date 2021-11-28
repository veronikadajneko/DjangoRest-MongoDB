from django.shortcuts import render

# Create your views here.

from models import QuickStar
from rest_framework import viewsets
from serializers import QuickStarSerializer

class QuickStarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = QuickStar.objects.order_by('_id')
    serializer_class = QuickStarSerializer
