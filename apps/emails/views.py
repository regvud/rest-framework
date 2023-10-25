from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email_service import EmailService


# Create your views here.
class EmailView(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(*args, **kwargs):
        EmailService.test_email()
        return Response('Good')
