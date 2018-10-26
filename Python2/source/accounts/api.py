from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginUserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated, )
