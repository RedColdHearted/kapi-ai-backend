import dataclasses
import json
import pathlib
import time

import jwt
import pydantic
import requests

YC_SE_ACCOUNT_CREDENTIALS = pathlib.Path("authorized_key.json")
JWT_ALGORITHM = "PS256"
YC_IAM_EXCHANGE_URL = (
    "https://iam.api.cloud.yandex.net/iam/v1/tokens"
)


@dataclasses.dataclass(frozen=True)
class SEAccountCredentials:
    """Represent dataclass of YC service-account credentials."""

    private_key: str
    key_id: str
    service_account_id: str


@dataclasses.dataclass(frozen=True)
class JWTPayload:
    """Represent dataclass of JWT payload for YC se-account."""

    aud: str
    iss: str
    iat: float
    exp: float


def _read_credentials(file_path: pathlib.Path) -> SEAccountCredentials:
    """Read and return se-account keys from json file."""
    with file_path.open() as credentials_file:
        obj = json.load(credentials_file)
        return SEAccountCredentials(
            private_key=obj["private_key"],
            key_id=obj["id"],
            service_account_id=obj["service_account_id"],
        )

def _create_payload(service_account_id: str) -> JWTPayload:
    """Create and return payload for jwt to iam token exchange."""
    now = int(time.time())
    return JWTPayload(
        aud=YC_IAM_EXCHANGE_URL,
        iss=service_account_id,
        iat=now,
        exp=now + 3600,
    )

def get_yc_iam_token() -> pydantic.SecretStr:
    """Return Yandex Cloud service-account IAM token as `pydantic.SecretStr`.

    Provides IAM token by exchange JWT from encoded credentials of
    service account stored in json file.

    """
    credentials = _read_credentials(YC_SE_ACCOUNT_CREDENTIALS)
    payload = _create_payload(credentials.service_account_id)

    response = requests.post(
        YC_IAM_EXCHANGE_URL,
        json={
            "jwt": jwt.encode(
                payload={
                    "aud": payload.aud,
                    "iss": payload.iss,
                    "iat": payload.iat,
                    "exp": payload.exp,
                },
                key=credentials.private_key,
                algorithm=JWT_ALGORITHM,
                headers={"kid": credentials.key_id},
            ),
        },
        headers={
            "Content-Type": "application/json",
        },
        timeout=3000,
    )
    response.raise_for_status()

    return pydantic.SecretStr(response.json()["iamToken"])
