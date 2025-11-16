from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
  """Manager or user profile"""

  def create_user(self, email, name, password=None):
    """Create a new user profile"""

    if not email:
      raise ValueError ('User must have email address')

    
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)
    
    # this will encrypt the password
    user.set_password(password)

    user.save(using=self._db)

    return user
  

  def create_superuser(self, email, name, password):
    """Create and save super user details"""
    user = self.create_user(email, name, password)

    user.is_admin = True
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Database model for user in the system"""

  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255) 
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)


  # Add the unique related_name and related_query_name arguments
  groups = models.ManyToManyField(
      Group,
      blank=True,
      help_text=(
          'The groups this user belongs to. A user will get all permissions '
          'granted to each of their groups.'
      ),
      related_name="profiles_manager_grp", # Unique related name
      related_query_name="profiles_manager_grp",
  )
  user_permissions = models.ManyToManyField(
      Permission,
      blank=True,
      help_text='Specific permissions for this user.',
      related_name="profiles_manager_perm", # Unique related name
      related_query_name="profiles_manager_perm",
  )


  # USER MODEL MANAGER CLASS
  objects = UserProfileManager()

  # using email as username_field
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """Return user full name"""
    return self.name
  
  def get_short_name(self):
    "Return Short name of User"
    return self.name

  def __str__(self):
    """Return string representation of USER"""
    return self.email


class ProfileFeedItem(models.Model):
  """Profile status update"""

  user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  status_text = models.CharField(max_length=255)
  created_on = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    """Return the model as string"""
    return self.status_text
























