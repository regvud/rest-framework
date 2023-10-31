from rest_framework import generics

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    