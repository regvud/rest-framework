from django.contrib.auth import get_user_model

from rest_framework import generics

from apps.users.serializers import UserSerializer

# Create your views here.
UserModel = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel
