import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key(key_path="secret.key"):
    key = AESGCM.generate_key(bit_length=256)

    with open(key_path, "wb") as key_file:
        key_file.write(key)

    print(f"[+] 256-bit AES key successfully generated and saved to '{key_path}'")
    return key

def load_key(key_path="secret.key"):

    with open(key_path, "rb") as key_file:
        return key_file.read()