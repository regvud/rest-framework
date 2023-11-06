from rest_framework import generics
from rest_framework.response import Response

from core.services.email_service import EmailService


class EmailView(generics.GenericAPIView):
    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response("ITS OKAY")
