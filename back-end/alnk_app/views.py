from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, Http404
from rest_framework import generics
import uuid
from .models import Link
from .serializers import LinkSerializer, UserSerializer


def user_link_view(request, linkeman):
    try:
        user_link = Link.objects.get(shortened_link=linkeman)
    except Exception:
        raise Http404
    return HttpResponseRedirect(user_link.original_link)


class ListLink(generics.ListCreateAPIView):
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        original_link=self.request.POST.get('original_link'),
                        shortened_link=uuid.uuid4().hex[:6])
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


class Userlist(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return get_user_model().objects.all()
        else:
            return get_user_model().objects.filter(username=self.request.user)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return get_user_model().objects.all()
        else:
            return get_user_model().objects.filter(username=self.request.user)
