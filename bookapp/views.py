from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from bookapp.models import BookShelf
from bookapp.serializers import BookShelfSerializer


class BookShelfView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    """ To get all book records"""
    def get(self, request, *args, **kwargs):
        books = BookShelf.objects.filter(permission_classes, request.user.data)
        serializer = BookShelfSerializer(serializer, many=True)

        return Resonse(serializer.data, status=status.HTTP_200_OK)
