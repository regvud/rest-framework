from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = UserSerializer(self.request.user)
        users = UserModel.objects.exclude(email=user['email'].value)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
