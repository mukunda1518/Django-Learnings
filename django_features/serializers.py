from django.contrib.auth.models import User
from rest_framework import serializers

from django_features.models import Merchant


class MerchantSerializerNormal(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    code = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"
        # fields = ["name", "code"]





