from rest_framework import serializers

class CompanyCompactSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    logo = serializers.ImageField()
    name = serializers.CharField(max_length=256)

class CompanySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    logo = serializers.ImageField()
    name = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=2048)
    site = serializers.CharField(max_length=256)
