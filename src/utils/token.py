import os
import jwt

def create_auth_token(payload: dict):
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise Exception("SECRET_KEY not defined.")

    return jwt.encode(
        payload=payload, 
        key=secret_key,
        algorithm="HS256",
    )

def validate_token(token: str | None) -> dict:
    from exceptions.auth_exceptions import InvalidTokenException
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise Exception("SECRET_KEY not defined.")

    if not token:
        raise InvalidTokenException()

    try:
        return jwt.decode(jwt=token, key=secret_key, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise InvalidTokenException()
    
