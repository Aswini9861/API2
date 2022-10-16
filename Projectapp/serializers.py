from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''serializer a name field for texting our APIviews'''
    name=serializers.CharField(max_length=10)
    