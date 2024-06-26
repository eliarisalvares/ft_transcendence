# Python STD library
from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID
import base64
import json

# Django
from django.utils import timezone


@dataclass
class JWTPayload:
    sub: UUID
    iat: float
    exp: float

    @staticmethod
    def create(sub: UUID, hours: int = 2):
        iat = timezone.now().timestamp()
        exp = (timezone.now() + timedelta(hours=hours)).timestamp()
        return JWTPayload(sub, iat, exp)

    @staticmethod
    def decode(base64payload: str):
        payload = json.loads(base64.b64decode(base64payload).decode("utf-8"))
        return JWTPayload(sub=payload["sub"], iat=payload["iat"], exp=payload["exp"])

    def is_expired(self):
        return timezone.now().timestamp() > self.exp

    def is_valid(self):
        return not self.is_expired()

    def to_dict(self):
        return {"sub": self.sub, "iat": self.iat, "exp": self.exp}

    def __timestamp_to_datetime(self, timestamp: float) -> str:
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        jwt_paylod = self.to_dict()
        iat = self.__timestamp_to_datetime(jwt_paylod["iat"])
        exp = self.__timestamp_to_datetime(jwt_paylod["exp"])
        return f"sub: {jwt_paylod['sub']}, iat: {iat}, exp: {exp}"
