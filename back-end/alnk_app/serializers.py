from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'owner', 'original_link', 'shortened_link' , 'date_created')