import stat

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer
from core.services.email_service import EmailService
from core.services.jwt_service import JwtService, RecoveryToken


class ShowMeView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class RecoverPasswordRequestView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    # provide email method
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)

        EmailService.recover_password(user)
        return Response("check email", status.HTTP_202_ACCEPTED)

    # id method
    # def get_object(self, *args, **kwargs):
    #     return UserModel.objects.get(pk=self.kwargs["pk"])
    # def post(self, *args, **kwargs):
    #     EmailService.recover_password(self.get_object())
    #     return Response("check email")


class RecoverPasswordView(generics.GenericAPIView):
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        new_password = self.request.data["new_password"]

        if not new_password:
            raise ValueError("Provide {'new_password' : '<password>'} ")

        user = JwtService.validate_token(self.kwargs["token"], RecoveryToken)

        user.set_password(new_password)
        user.save()

        return Response("password has been changed", status.HTTP_202_ACCEPTED)
