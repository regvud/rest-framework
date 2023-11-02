import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from apps.users.models import UserModel
from core.dataclasses.user_dataclass import UserDataclass
from core.services.jwt_service import ActivateToken, JwtService, RecoveryToken


class EmailService:
    def __send_email(to: str, template_name: str, context: {}, subject=""):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def test_email(cls):
        cls.__send_email("skilide.skilide@gmail.com", "test_email.html", {}, "Hello")

    @classmethod
    def register_email(cls, user: UserDataclass):
        token = JwtService.create_token(user, ActivateToken)
        url = f"http://localhost:3000/activate/{token}"
        cls.__send_email(
            user.email,
            "register.html",
            {"name": user.email, "url": url},
            "EMAIL ACCOUNT REGISTRATION",
        )

    @classmethod
    def recover_password(cls, email, data):
        user = UserModel.objects.filter(user["email"] == email)
        token = JwtService.create_token(user, RecoveryToken)
        pass
