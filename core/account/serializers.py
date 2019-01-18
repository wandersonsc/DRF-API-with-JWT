from rest_framework.serializers import EmailField, ModelSerializer, ValidationError
from rest_framework.validators import UniqueValidator

from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    """ Create a serializer for all user profile objects. """
    
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
                'write_only':True,
                'max_length':128,
                'min_length':5,
                'required':True
            }
        }
    
    def validate_name(self, value):
        """ Make sure that name is unique. """ 

        qs = UserProfile.objects.filter(name__iexact=value)
        if qs:
            raise ValidationError("A user with that name already exists. ")
        return value


    def create(self, validated_data):
        """ Create and return a new user. """

        user = UserProfile(
            name    = validated_data['name'],
            email   = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user