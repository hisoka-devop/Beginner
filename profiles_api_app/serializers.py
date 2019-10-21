from rest_framework import serializers
from profiles_api_app import models

class HelloSerializer(serializers.Serializer):
    '''creation of a serializer to be able to further post data'''
    name = serializers.CharField(max_length=20)

class UserProfileSerializer(serializers.ModelSerializer):
    '''A user profile model serializer that addresses the creation of managing the user profiles'''
    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password':{
            'write_only':True,
            'style':{
                'input_type':'password'
            }
        }}

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(email=validated_data['email'], name=validated_data['name'],password=validated_data['password'])
        print(str(validated_data['name']))
        return user
