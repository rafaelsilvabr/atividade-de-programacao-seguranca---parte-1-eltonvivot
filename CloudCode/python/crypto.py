from cryptography.fernet import Fernet
import json

def read_write_json(data: dict = None, filename="credentials.json") -> dict:
    if data is None:
        with open(filename, 'r') as f:
            data = json.load(f)
    else:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    return data


def create_or_login(login, password):
  data = read_write_json()
  if login in data:
    return user_login(login, password)
  else:
    data[login] = password
    read_write_json(data)
  return "User created successfully."

def user_login(login, password):
  data = read_write_json()
  if not login in data:
    return "User does not exists."
  if data[login] != password:
    return "Wrong password."
  return True

# --

def generate_key():
  return Fernet.generate_key()

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def decrypt_middleware(message: str, key: bytes):
  decrypt_msg = decrypt(message, key)
  return json.loads(decrypt_msg.decode())

def encrypt_middleware(message: dict, key: bytes):
  message_str = json.dumps(message)
  return encrypt(message_str.encode(), key)

