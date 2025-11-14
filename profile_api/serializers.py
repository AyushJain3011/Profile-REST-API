
from rest_framework import serializers



class HelloSerializer(serializers.Serializer):
  """Serializer a name filed for testing for our api view"""

  name = serializers.CharField(max_length=10)









