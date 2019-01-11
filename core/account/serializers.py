from rest_framework.serializers import EmailField, ModelSerializer, ValidationError
from rest_framework.validators import UniqueValidator

from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    """ Create a serializer for all user profile objects """
    
    email: EmailField(
        required=True, 
        validators=[
            UniqueValidator(queryset=UserProfile.objects.all(), message="This email already exist.")
        ]
    )

    class Meta:
        model = UserProfile
        fields =(
            'id',
            'name',
            'email',
            'password'
        )
        extra_kwargs = {
            'password':{
                'read_only':True,
                'max_length':128,
                'min_length':5,
                'required':True
            }
        }
