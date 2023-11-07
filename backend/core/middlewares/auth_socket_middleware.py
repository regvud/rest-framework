from channels.middleware import BaseMiddleware


class AuthSocketMiddleware(BaseMiddleware):
    def __call__(self, scope, receive, send):
        query_token = dict(
            [
                item.split("=")
                for item in scope["query_string"].decode("utf-8").split("&")
                if item
            ]
        ).get("token", None)
        print(query_token)
        return super().__call__(scope, receive, send)
