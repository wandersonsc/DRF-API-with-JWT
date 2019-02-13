from django.conf import settings
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileAPIView(CreateAPIView):
    """ Handles creating profiles & Allow any user (authenticated or not) to access this endpoint"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny, )
