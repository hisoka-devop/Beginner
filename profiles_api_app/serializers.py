from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''creation of a serializer to be able to further post data'''
    name = serializers.CharField(max_length=20)
