from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'owner', 'original_link', 'shortened_link',
                 'date_created')


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'last_login')
