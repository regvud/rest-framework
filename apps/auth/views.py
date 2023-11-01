from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


class ShowMeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
