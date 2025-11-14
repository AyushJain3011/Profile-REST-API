from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Testing rest api"""

  def get(self, request, format=None):
    """Return a list of ApiViews Features"""

    an_apiview = [
      'Uses http funtions as methods',
      'Is similar to traditionl Django View',
      'Give you most control over you app',
      'is mapped manually URLs',
    ]

    # every https func must have a response b/c it is reuired to return a response in django framework
    # Every response must be a List or Dict b/c it's converted into JSON
    return Response({'message': 'Hello', 'an_apiview': an_apiview})

