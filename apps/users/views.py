from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import ProfileSerializer, UserSerializer

from core.permissions import IsAdminOrWriteOnly, IsSuperUser

from .models import ProfileModel, UserModel


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticated(),)
        return (IsAdminOrWriteOnly(),)


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()


class FromUserToAdminView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_staff == 0:
            user.is_staff = 1
            user.save()

            user = self.serializer_class(user)
            return Response(user.data, status.HTTP_200_OK)
        return Response(f'{user} is already admin', status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_object()).data, status=200)


class FromAdminToUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_staff == 1:
            user.is_staff = 0
            user.save()

            user = self.serializer_class(user)
            return Response(user.data, status.HTTP_200_OK)
        return Response(f'{user} is not admin anymore', status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        return Response(self.serializer_class(self.get_object()).data, status=200)


class UserBlockView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):
        user_to_block = self.get_object()
        option = self.request.data['user']
        if not option:
            return Response('Provide user: "user":"block" or "user":"unblock"', status.HTTP_200_OK)

        match option:
            case 'block':
                if user_to_block.is_active == 1:
                    user_to_block.is_active = 0
                    user_to_block.save()

                    user_to_block = self.serializer_class(user_to_block)
                    return Response(user_to_block.data, status.HTTP_200_OK)

            case 'unblock':
                if user_to_block.is_active == 0:
                    user_to_block.is_active = 1
                    user_to_block.save()

                    user_to_block = self.serializer_class(user_to_block)
                    return Response(user_to_block.data, status.HTTP_200_OK)

        return Response(f'{user_to_block}s: {option}ed', status.HTTP_200_OK)
