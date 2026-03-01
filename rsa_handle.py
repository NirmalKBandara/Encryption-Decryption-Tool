from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

import os

def generate_keypair(private_key_path='private_key.pem', public_key_path='public_key.pem'):
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    with open(private_key_path, 'wb') as file:
        file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.privateFormat.PKCS8,
                encryption_algorithem=serialization.NoEncryption()
            )
        )

    with open(public_key_path, 'wb') as file:
        file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.publicFormat.SubjectPublicKeyInfo,
            )
        )

    print(f"[+] RSA Key pair generated: '{private_key_path}' and '{public_key_path}'")
    return private_key, public_key

def load_private_key(private_key_path="private_key.pem"):
    if not os.path.exists(private_key_path):
        raise FileNotFoundError(f"[-] Private key not found at {private_key_path}")

    with open(private_key_path, "rb") as file:
        return serialization.load_pem_private_key(
            file.read(),
            password=None
        )
 
def load_public_key(public_key_path="public_key.pem"):
    if not os.path.exists(public_key_path):
        raise FileNotFoundError(f"[-] Public key not found at {public_key_path}")

    with open(public_key_path, "rb") as file:
        return serialization.load_pem_public_key(file.read())

