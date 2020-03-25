from django.shortcuts import render
from .models import Link
from rest_framework import generics
from .serializers import LinkSerializer


class ListLink(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class DetailLink(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

