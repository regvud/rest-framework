import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import ActivateToken, JwtService


class EmailService:
    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject: ''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('email_host_user'), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def test_email(cls):
        cls.__send_email('skilide.skilide@gmail.com',
                         'test_email.html',
                         {},
                         'hello from ivan')

    @classmethod
    def register_email(cls, user: UserDataClass):
        token = JwtService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'

        cls.__send_email(
            user.email,
            'register.html',
            {'name': user.profile.name, 'url': url},
            'Register'
        )
