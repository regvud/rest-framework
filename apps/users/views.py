from rest_framework import generics, status
from rest_framework.response import Response

from apps.parks.serializers import ParkSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserParkCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()
        park = self.request.data
        serializer = ParkSerializer(data=park)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status.HTTP_201_CREATED)
