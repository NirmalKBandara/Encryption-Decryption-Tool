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

