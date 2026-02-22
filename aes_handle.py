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

def encrypt_file(file_path, key):
    aes_object = AESGCM(key)
    nonce = os.urandom(12)

    with open(file_path, "rb") as file:
        plaintext = file.read()

    cipertext = aes_object.encrypt(nonce, plaintext, None)
    encrypt_file_path = file_path + ".env"

    with open(encrypt_file_path, "wb") as file:
        file.write(nonce + cipertext)

    print(f"[+] Successfully encrypted '{file_path}' to '{encrypted_file_path}'")