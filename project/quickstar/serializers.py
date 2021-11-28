from models import QuickStar
from rest_framework import serializers


class QuickStarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuickStar
        fields = ['_id', 'Textual_paragraph', 'author', 'date']