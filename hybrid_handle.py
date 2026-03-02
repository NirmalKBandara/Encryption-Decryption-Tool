import os
import struct
import rsa_handle
import aes_handle
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def hybrid_encrypt(file_path, public_key_path="public_key.pem"):
    
    aes_key = AESGCM.generate_key(bit_length=256)

    with open(file_path, "rb") as f:
        plaintext = f.read()

    aes_object = AESGCM(aes_key)
    nonce = os.urandom(12)
    aes_ciphertext = aes_object.encrypt(nonce, plaintext, None)

    public_key = rsa_handle.load_public_key(public_key_path)
    encrypted_aes_key = rsa_handle.encrypt_data(aes_key, public_key)

    encrypted_file_path = file_path + ".henc"
    rsa_block_size = len(encrypted_aes_key)

    with open(encrypted_file_path, "wb") as f:
        f.write(struct.pack(">H", rsa_block_size))  # :) (big-endian)
        f.write(encrypted_aes_key)                   
        f.write(nonce)                               
        f.write(aes_ciphertext)                      

    print(f"[+] Hybrid encrypted '{file_path}' → '{encrypted_file_path}'")


def hybrid_decrypt(encrypted_file_path, private_key_path="private_key.pem"):
    
    with open(encrypted_file_path, "rb") as f:
        
        rsa_block_size = struct.unpack(">H", f.read(2))[0]  
        encrypted_aes_key = f.read(rsa_block_size)          
        nonce = f.read(12)                                  
        aes_ciphertext = f.read()                          

    
    private_key = rsa_handle.load_private_key(private_key_path)
    aes_key = rsa_handle.decrypt_data(encrypted_aes_key, private_key)

    aes_object = AESGCM(aes_key)
    plaintext = aes_object.decrypt(nonce, aes_ciphertext, None)

    decrypted_file_path = encrypted_file_path.replace(".henc", ".hdec")
    with open(decrypted_file_path, "wb") as f:
        f.write(plaintext)

    print(f"[+] Hybrid decrypted '{encrypted_file_path}' → '{decrypted_file_path}'")
