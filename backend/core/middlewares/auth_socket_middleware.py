from channels.middleware import BaseMiddleware


class AuthSocketMiddleware(BaseMiddleware):
    def __call__(self, scope, receive, send):
        return super().__call__(scope, receive, send)
