from typing import Type

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from core.enums.jwt_enum import ActionTokenEnum

UserModel = get_user_model()
ActionTokenClassType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class JwtService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            res = token_class(token)
            res.check_blacklist()
        except Exception as err:
            print(err)

        res.blacklist()
        user_id = res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
