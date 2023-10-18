from rest_framework import generics
from rest_framework.response import Response

from apps.users.serializers import UserSerializer


class Me(generics.GenericAPIView):
    def get(self, *args, **kwargs):
        me = self.request.user
        serializer = UserSerializer(me)
        return Response(serializer.data, status=200)
