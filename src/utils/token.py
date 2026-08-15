import os
import jwt

def create_auth_token(user_id):
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise Exception("SECRET_KEY not defined.")
    
    payload = {
        'user_id': user_id
    }

    return jwt.encode(
        payload=payload, 
        key=secret_key,
        algorithm="HS256",
    )
