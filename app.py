import aes_handle
import rsa_handle
import hybrid_handle
import os
import sys

def main():
    print("=== Encryption/Decryption Tool ===")
    
    while True:
        print("\nAlgorithms:")
        print("1. AES (Advanced Encryption Standard)")
        print("2. RSA (Rivest-Shamir-Adleman)")
        print("3. Hybrid (RSA + AES)")
        print("4. Exit")
        
        algo_choice = input("Select an algorithm (1-4): ").strip()
        
        if algo_choice == '1':
            while True:
                print("\nAES Options:")
                print("1. Generate a new key")
                print("2. Encrypt a file")
                print("3. Decrypt a file")
                print("4. Back to main menu")
                
                choice = input("Select an option (1-4): ").strip()
                
                if choice == '1':
                    key_path = input("Enter path to save key (default: secret.key): ").strip() or "secret.key"
                    try:
                        aes_handle.generate_key(key_path)
                    except Exception as e:
                        print(f"[-] Error generating key: {e}")
                        
                elif choice == '2':
                    file_path = input("Enter path of the file to encrypt: ").strip()
                    if not os.path.exists(file_path):
                        print(f"[-] File not found: '{file_path}'")
                        continue
                        
                    key_path = input("Enter path to the key file (default: secret.key): ").strip() or "secret.key"
                    if not os.path.exists(key_path):
                        print(f"[-] Key file not found: '{key_path}'")
                        continue
                        
                    try:
                        key = aes_handle.load_key(key_path)
                        aes_handle.encrypt_file(file_path, key)
                    except Exception as e:
                        print(f"[-] Encryption failed: {e}")
                        
                elif choice == '3':
                    file_path = input("Enter path of the file to decrypt: ").strip()
                    if not os.path.exists(file_path):
                        print(f"[-] File not found: '{file_path}'")
                        continue
                        
                    key_path = input("Enter path to the key file (default: secret.key): ").strip() or "secret.key"
                    if not os.path.exists(key_path):
                        print(f"[-] Key file not found: '{key_path}'")
                        continue
                        
                    try:
                        key = aes_handle.load_key(key_path)
                        aes_handle.decrypt_file(file_path, key)
                    except Exception as e:
                        print(f"[-] Decryption failed. Did you use the wrong key/file? Error: {e}")
                        
                elif choice == '4':
                    break
                    
                else:
                    print("[-] Invalid choice. Please enter 1, 2, 3, or 4.")

        elif algo_choice == '2':
            while True:
                print("\nRSA Options:")
                print("1. Generate key pair")
                print("2. Encrypt text")
                print("3. Decrypt text")
                print("4. Back to main menu")
                
                choice = input("Select an option (1-4): ").strip()
                
                if choice == '1':
                    private_path = input("Enter path to save private key (default: private_key.pem): ").strip() or "private_key.pem"
                    public_path = input("Enter path to save public key (default: public_key.pem): ").strip() or "public_key.pem"
                    try:
                        rsa_handle.generate_keypair(private_path, public_path)
                    except Exception as e:
                        print(f"[-] Error generating RSA keys: {e}")
                        
                elif choice == '2':
                    text = input("Enter text to encrypt: ").strip()
                    public_key_path = input("Enter path to the public key (default: public_key.pem): ").strip() or "public_key.pem"
                    
                    if not os.path.exists(public_key_path):
                        print(f"[-] Public key file not found: '{public_key_path}'")
                        continue
                        
                    try:
                        public_key = rsa_handle.load_public_key(public_key_path)
                        ciphertext = rsa_handle.encrypt_data(text.encode('utf-8'), public_key)
                        
                        out_path = input("Enter path to save ciphertext (default: rsa_ciphertext.bin): ").strip() or "rsa_ciphertext.bin"
                        with open(out_path, 'wb') as f:
                            f.write(ciphertext)
                        print(f"[+] Encrypted data saved to '{out_path}'")
                    except Exception as e:
                        print(f"[-] Encryption failed: {e}")
                        
                elif choice == '3':
                    in_path = input("Enter path of the ciphertext file to decrypt (default: rsa_ciphertext.bin): ").strip() or "rsa_ciphertext.bin"
                    if not os.path.exists(in_path):
                        print(f"[-] File not found: '{in_path}'")
                        continue
                        
                    private_key_path = input("Enter path to the private key (default: private_key.pem): ").strip() or "private_key.pem"
                    if not os.path.exists(private_key_path):
                        print(f"[-] Private key file not found: '{private_key_path}'")
                        continue
                        
                    try:
                        private_key = rsa_handle.load_private_key(private_key_path)
                        with open(in_path, 'rb') as f:
                            ciphertext = f.read()
                        plaintext = rsa_handle.decrypt_data(ciphertext, private_key)
                        print(f"[+] Decrypted text: {plaintext.decode('utf-8')}")
                    except Exception as e:
                        print(f"[-] Decryption failed. Did you use the wrong key/file? Error: {e}")

                elif choice == '4':
                    break
                    
                else:
                    print("[-] Invalid choice. Please enter 1, 2, 3, or 4.")

        elif algo_choice == '3':
            while True:
                print("\nHybrid (RSA + AES) Options:")
                print("1. Encrypt a file")
                print("2. Decrypt a file")
                print("3. Back to main menu")

                choice = input("Select an option (1-3): ").strip()

                if choice == '1':
                    file_path = input("Enter path of the file to encrypt: ").strip()
                    if not os.path.exists(file_path):
                        print(f"[-] File not found: '{file_path}'")
                        continue

                    public_key_path = input("Enter path to the RSA public key (default: public_key.pem): ").strip() or "public_key.pem"
                    if not os.path.exists(public_key_path):
                        print(f"[-] Public key file not found: '{public_key_path}'")
                        continue

                    try:
                        hybrid_handle.hybrid_encrypt(file_path, public_key_path)
                    except Exception as e:
                        print(f"[-] Hybrid encryption failed: {e}")

                elif choice == '2':
                    file_path = input("Enter path of the .henc file to decrypt: ").strip()
                    if not os.path.exists(file_path):
                        print(f"[-] File not found: '{file_path}'")
                        continue

                    private_key_path = input("Enter path to the RSA private key (default: private_key.pem): ").strip() or "private_key.pem"
                    if not os.path.exists(private_key_path):
                        print(f"[-] Private key file not found: '{private_key_path}'")
                        continue

                    try:
                        hybrid_handle.hybrid_decrypt(file_path, private_key_path)
                    except Exception as e:
                        print(f"[-] Hybrid decryption failed. Wrong key or corrupted file? Error: {e}")

                elif choice == '3':
                    break

                else:
                    print("[-] Invalid choice. Please enter 1, 2, or 3.")

        elif algo_choice == '4':
            print("Exiting tool...")
            sys.exit(0)

        else:
            print("[-] Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()