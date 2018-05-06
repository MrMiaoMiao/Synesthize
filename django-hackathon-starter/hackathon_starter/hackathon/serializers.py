from django.forms import widgets
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'code', 'linenos')