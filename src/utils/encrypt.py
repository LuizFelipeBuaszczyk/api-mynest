
def encrypt_password(password: str):
    import hashlib
    from utils.settings import ENCRYPT_KEY

    return hashlib.sha256(f"{password}{ENCRYPT_KEY}".encode('utf-8')).hexdigest()

