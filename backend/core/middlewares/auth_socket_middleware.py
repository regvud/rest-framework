from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from core.services.jwt_service import JwtService, SocketToken


@database_sync_to_async
def get_user(token):
    try:
        return JwtService.validate_token(token, SocketToken)
    except (Exception,):
        return


class AuthSocketMiddleware(BaseMiddleware):
    def __call__(self, scope, receive, send):
        query_token = dict(
            [
                item.split("=")
                for item in scope["query_string"].decode("utf-8").split("&")
                if item
            ]
        ).get("token", None)
        scope["user"] = get_user(query_token) if query_token else None
        print(scope["user"])
        print(query_token)
        return super().__call__(scope, receive, send)
