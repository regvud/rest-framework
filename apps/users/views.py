from rest_framework import generics

from apps.users.serializers import UserModel, UserSerializer


# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()