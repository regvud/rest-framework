from typing import Type

from core.dataclasses.user_dataclass import UserDataclass
from core.enums.action_token_enum import ActionTokenEnum
from rest_framework.authentication import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import BlacklistMixin, Token

UserModel = get_user_model()
ActionTokenType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.lifetime


class SocketToken(ActionToken):
    token_type = ActionTokenEnum.SOCKET.token_type
    lifetime = ActionTokenEnum.SOCKET.lifetime


class JwtService:
    @staticmethod
    def create_token(user: UserDataclass, token_class: ActionTokenType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenType):
        try:
            res = token_class(token)
            res.check_blacklist()
        except Exception:
            raise Exception

        res.blacklist()
        user_id = res.payload.get("user_id")

        return get_object_or_404(UserModel, pk=user_id)
