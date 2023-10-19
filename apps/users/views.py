from rest_framework import generics

from apps.users.serializers import ProfileSerializer, UserSerializer

from .models import ProfileModel, UserModel


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()
