from rest_framework import serializers
from .models import *


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    data = DataSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('__all__')


