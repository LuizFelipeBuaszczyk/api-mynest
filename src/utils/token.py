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
