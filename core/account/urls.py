from django.urls import path

from .views import UserProfileAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserProfileAPIView.as_view(), name='register'),

]