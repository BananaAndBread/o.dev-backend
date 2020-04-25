from rest_framework import serializers
from rest_framework.fields import DictField, FloatField, CharField


class RequestSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    currency = CharField()


class StatisticsSerializer(serializers.Serializer):
    std_dev = FloatField()
    avg = FloatField()
    cor = DictField(child=FloatField())


class ResponseSerializer(serializers.Serializer):
    document = DictField(child=StatisticsSerializer())
