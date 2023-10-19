from rest_framework import generics
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


# Create your views here.
class MeView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        me = self.request.user
        return Response(self.serializer_class(me).data, status=200)
