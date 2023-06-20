from cryptography.fernet import Fernet
import json, const

def encrypt(message: str, key: bytes = const.FERNET_KEY) -> bytes:
    return Fernet(key).encrypt(message.encode())

def decrypt(token: bytes, key: bytes = const.FERNET_KEY) -> bytes:
    return Fernet(key).decrypt(token)

