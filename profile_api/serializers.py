
from rest_framework import serializers

from . import models

# for ApiViewset
class HelloSerializer(serializers.Serializer):
  """Serializer a name filed for testing for our api view"""

  name = serializers.CharField(max_length=10)


# for ViewSet
class UserProfileSerializer(serializers.ModelSerializer):
  """Serializers user profile object"""

  class Meta:
    model = models.UserProfile

    # list of fields we are going to manage in our serializer and those will be accessible in our APi
    fields = ('id', 'email', 'name', 'password')
    extra_kwargs = {
      'password': {
          'write_only':True,
          'style':{
            'input_type': 'password'
          }
      }
    }


  def create(self, validated_data):
    """Create a new User """

    user = models.UserProfile.objects.create_user(
      email=validated_data['email'],
      name=validated_data['name'],
      password=validated_data['password'],
    )

    return user
  

  def update(self, instance, validated_data):
        """Handle updating user account"""
        
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)












