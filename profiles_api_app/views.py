from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
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
                            status=status.HTTP_400_BAD_REQUEST,
                            )

    def put(self, request, pk=None):
        '''To update full objects'''
        return Response(
            {
                'Method': 'PUT',
            }
        )

    def patch(self, request, pk=None):
        '''To udpate objects partially'''
        return Response(
            {
                'Method': 'PATCH',
            }
        )

    def delete(self, request, pk=None):
        '''To delete an object fully'''
        return Response(
            {
                'Method': 'DELETE',
            }
        )


class HelloViewSet(viewsets.ViewSet):
    '''A class to handle the the viewsets'''
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''A simple implementation of an easy list'''
        a_viewset = [
            'User Actions: list, create, retrieve, update, partial_update',
            'It uses Routers rather than normal urlpatterns.path',
            'Provides more functionality with less code'
        ]

        return Response({
            'msg': 'Greetings',
            'a_viewset': a_viewset
        })

    def create(self, request):
        '''A simple implementation of creating a new object, POST alternative'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({
                'msg': f'Hello {name}',
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)

    def retrieve(self, request, pk=None):
        '''A simple implementation of get, getting a specified object'''
        return Response({
            'Method': 'GET',
        })

    def update(self, request, pk=None):
        '''A simple implementation of update, which is the replacement of PUT'''
        return Response({
            'Method': 'PUT',
        })

    def partial_update(self, request, pk=None):
        '''A simple implementation of partial_update, which is the replacement of PATCH'''
        return Response({
            'Method': 'PATCH',
        })

    def destroy(self, request, pk=None):
        '''A simple implementation of destroy, which is the replacement of the delete'''
        return Response({
            'Method':'DELETE'
        })
