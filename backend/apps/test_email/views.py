from core.services.email_service import EmailService

from rest_framework import generics
from rest_framework.response import Response


class TestEmailView(generics.GenericAPIView):
    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response("okich")
