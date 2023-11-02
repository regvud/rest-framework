from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class ShowMeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class RecoverPasswordView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get_object(self, *args, **kwargs):
        return UserModel.objects.get(pk=self.kwargs["pk"])

    def post(self, *args, **kwargs):
        new_password = self.request.data["new_password"]

        if not new_password:
            raise ValueError("Provide 'new_password' : ' ...password ' ")

        user = self.get_object()
        user.set_password(new_password)
        user.save()

        return Response("ok")
