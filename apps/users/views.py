from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


# Create your views here.
class UserCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return (IsAuthenticated(),)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)
