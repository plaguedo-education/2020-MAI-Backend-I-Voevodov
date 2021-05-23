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

class VacancyCompactSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=256)
    companie = serializers.UUIDField()
    wage_from = serializers.IntegerField()
    wage_up_to = serializers.IntegerField()
    published_date = serializers.DateTimeField()

class VacancySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=256)
    companie = serializers.UUIDField()
    description = serializers.CharField(max_length=2048)
    wage_from = serializers.IntegerField()
    wage_up_to = serializers.IntegerField()
    published_date = serializers.DateTimeField()
