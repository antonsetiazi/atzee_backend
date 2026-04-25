from urllib.parse import parse_qs

from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from core.users.models import User


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        scope["user"] = AnonymousUser()

        try:
            query_string = scope["query_string"].decode()
            params = parse_qs(query_string)
            token = params.get("token", [None])[0]

            if token:
                # validasi signature + exp
                validated = UntypedToken(token)

                payload = validated.payload

                # hanya access token boleh websocket
                if payload.get("token_type") != "access":
                    raise InvalidToken("Only access token allowed")

                user_id = payload.get("user_id")

                if user_id:
                    scope["user"] = await get_user(user_id)

        except (InvalidToken, TokenError) as e:
            print("JWT WS ERROR:", e)
        except Exception as e:
            print("WS UNKNOWN ERROR:", e)

        return await self.app(scope, receive, send)