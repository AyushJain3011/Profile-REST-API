from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers



class HelloApiView(APIView):
  """Testing rest api"""

  # for post, put, patch request
  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Return a list of ApiViews Features"""

    an_apiview = [
      'Uses http funtions as methods',
      'Is similar to traditionl Django View',
      'Give you most control over you app',
      'is mapped manually URLs',
    ]

    # every https func must have a response b/c it is required to return a response in django framework
    # Every response must be a List or Dict b/c it's converted into JSON
    return Response({'message': 'Hello', 'an_apiview': an_apiview})



  def post(self, request):
    """Create a hello message with our name"""

    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():

      name = serializer.validated_data.get('name')
      message = f'Hello {name}'

      return Response({'message': message})
    
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )
    
  def put(self, request, pk=None):
    """Handle updating an object"""

    return Response({'method': 'PUT'})
  

  def patch(self, reqeust, pk=None):
    """Handle Partially updating an object it's means a field"""

    return Response({'method': 'PATCH'})
  

  def delete(self, reqeust, pk=None):
    """Delete an object on the bases of object primary key"""

    return Response({'method':'DELETE'})


