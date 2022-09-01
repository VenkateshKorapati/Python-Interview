from rest_framework import serializers
from bookapp.models import BookShelf
from rest_framework.response import Response
from rest_framework import status


class BookShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookShelf
        fields='__all__'
