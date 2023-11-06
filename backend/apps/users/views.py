from apps.users.serializers import UserSerializer
from rest_framework import generics
from rest_framework.authentication import get_user_model

UserModel = get_user_model()


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = UserModel
    serializer_class = UserSerializer
