from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api_app import serializers

# Create your views here.
class HelloApiView(APIView):
    """
    A class of the APIView to return simple hello world and message
    """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Args:
            self (APIView object): self
            request (APIView request object): the request received

        Returns:
            Response: it returns the response of the API in a dictionary format

        """
        msg = [
            'Uses HTTP Methods',
            'Similar to traditional http websites',
            'Gives you Control over Application'
            ]

        return Response({
            'message': 'Hello to the API World',
            'api_view': msg})

    def post(self, request):
        """
        the function receives a name post and return a greeting.
        Args:
            request: The request received
        Returns:
            Response: Holding either the Hello Name submitted or a response code of 404
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            greetings = f'Hello {name}'
            return Response({
                'Greetings': greetings
            })
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST,
                            )

    def put(self, request, pk=None):
        '''To update full objects'''
        return Response(
            {
                'Method':'PUT',
            }
        )

    def patch(self, request, pk=None):
        '''To udpate objects partially'''
        return Response(
            {
                'Method':'PATCH',
            }
        )

    def delete(self, request, pk=None):
        '''To delete an object fully'''
        return Response(
            {
                'Method':'DELETE',
            }
        )
