from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from profile_api import models
from rest_framework.authentication import TokenAuthentication
from . import permission
from rest_framework import filters


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
  

  def patch(self, request, pk=None):
    """Handle Partially updating an object it's means a field"""

    return Response({'method': 'PATCH'})
  

  def delete(self, request, pk=None):
    """Delete an object on the bases of object primary key"""

    return Response({'method':'DELETE'})
  




# we create action which we are going top perform on our end-point or database
class HelloViewSet(viewsets.ViewSet):
  """Test Api view set"""

  serializer_class = serializers.HelloSerializer

  # Retrive multiple instanses
  def list(self, request):

    a_viewset = [
      'Uses action (create, reterive, update, partial update, destroy)',
      'Automatically  maps  the URLs using Routers',
      'Provide more functionality with less code'
    ]

    return Response({'Message': 'Hello', 'a_viewset': a_viewset})
  
  # create a new instance
  def create(self, request):
    """create a new hello message"""

    serealizer = self.serializer_class(data=request.data)

    if serealizer.is_valid():
      name = serealizer.validated_data.get('name')

      return Response({'message': f'Hello {name}!'})
    
    else:
      return Response(
        serealizer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
    
    # Reterive one instance 
  def reterive(self, request, pk=None):
    """Handle getting object by ID"""

    return Response({'HTTP Method': 'GET'})
  

  def update(self, request, pk=None):
    """update an object on the bases of id"""

    return Response({'HTTP Method': 'PUT'})
  
  def partial_update(self, request, pk=None):
    """handle updating part of an object"""

    return Response({'HTTP Method': 'PATCH'})
  
  def destroy(self, request, pk=None):
    """Handle destroing an object using PK"""

    return Response({'Http Method': 'DELETE'})
                      

class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating user profiles"""

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()

  # authetication mechanism
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permission.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,) 
  search_fields = ('name', 'email',)

  





