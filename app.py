import aes_handle
import os
import sys

def main():
    print("=== AES-GCM Encryption/Decryption Tool ===")
    
    while True:
        print("\nOptions:")
        print("1. Generate a new key")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")
        
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
            print("Exiting tool...")
            sys.exit(0)
            
        else:
            print("[-] Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()