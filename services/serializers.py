from rest_framework import serializers
from .models import (
    Areas,
    Sedes,
    AreasSedes,
    Categories
)

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = '__all__'

class AreaSedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasSedes
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'