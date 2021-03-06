from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, Http404
from rest_framework import generics
import uuid
from user_agents import parse
from .models import Link, LinkView
from .serializers import LinkSerializer, UserSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxy = True
        ip = x_forwarded_for.split(',')[0]
    else:
        proxy = False
        ip = request.META.get('REMOTE_ADDR')
    return ip, proxy


def user_link_view(request, linkeman):
    try:
        user_link = Link.objects.get(shortened_link=linkeman)
        user_agent = parse(request.META.get('HTTP_USER_AGENT'))
        ip, proxy_status = get_client_ip(request)
        view = LinkView()
        view.requestor_browser = user_agent.browser
        view.requestor_device = user_agent.device
        view.requestor_ip = ip
        view.requestor_link = user_link
        view.requestor_os = user_agent.os
        if user_agent.is_bot:
            view.requestor_identity = "invalid-user: Bot"
        else:
            view.requestor_identity = "valid-user"
        if proxy_status:
            view.requestor_connection = "Proxy Ip"
        else:
            view.requestor_connection = "Real Ip"
        view.save()
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
