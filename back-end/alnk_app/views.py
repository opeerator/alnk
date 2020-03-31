from django.shortcuts import render
from .models import Link
from rest_framework import generics
from .serializers import LinkSerializer


class ListLink(generics.ListCreateAPIView):
    serializer_class = LinkSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Link.objects.all()
        else:
            return Link.objects.filter(owner=self.request.user)


class DetailLink(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LinkSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Link.objects.all()
        else:
            return Link.objects.filter(owner=self.request.user)
