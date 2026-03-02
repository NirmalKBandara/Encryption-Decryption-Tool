# Encryption-Decryption Tool

A command-line Python tool for learning and applying standard cryptographic algorithms: AES, RSA, and Hybrid (RSA + AES) encryption.

## Algorithms

### AES (Advanced Encryption Standard)
Symmetric encryption using AES-256-GCM. A single secret key is used to both encrypt and decrypt files. Fast and suitable for files of any size.

### RSA (Rivest-Shamir-Adleman)
Asymmetric encryption using a 2048-bit RSA key pair. The public key encrypts data and the private key decrypts it. Limited to small data (up to 190 bytes) due to RSA's block size constraint.

### Hybrid (RSA + AES)
Combines both algorithms. A random AES key encrypts the file, and the RSA public key encrypts that AES key. The recipient uses their RSA private key to recover the AES key and decrypt the file. Supports files of any size.

## Project Structure

```
Encryption-Decryption-Tool/
├── app.py              # Main CLI entry point
├── aes_handle.py       # AES key generation, file encryption/decryption
├── rsa_handle.py       # RSA key generation, data encryption/decryption
├── hybrid_handle.py    # Hybrid (RSA + AES) file encryption/decryption
├── test_rsa.py         # Automated unit tests for the RSA module
├── requirements.txt    # Python dependencies
└── Dockerfile          # Docker container setup
```

## Requirements

- Python 3.11+
- `cryptography >= 42.0.5`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool:

```bash
python app.py
```

A menu will prompt you to choose an algorithm and operation. Follow the on-screen instructions to generate keys, encrypt, or decrypt.

### AES Workflow
1. Select **AES** from the main menu.
2. Generate a key (saved as `.key` file).
3. Encrypt a file (output: `<filename>.enc`).
4. Decrypt a file (output: `<filename>.dec`).

### RSA Workflow
1. Select **RSA** from the main menu.
2. Generate a key pair (saved as `private_key.pem` and `public_key.pem`).
3. Encrypt text using the public key (output saved as a `.bin` file).
4. Decrypt using the private key.

### Hybrid Workflow
1. Select **Hybrid (RSA + AES)** from the main menu.
2. Provide the file to encrypt and the RSA public key path.
3. Output is saved as `<filename>.henc`.
4. Decrypt using the RSA private key to recover the original file (output: `<filename>.hdec`).

## Running with Docker

Build the image:

```bash
docker build -t encryption-tool .
```

Run interactively:

```bash
docker run -it --rm -v "${PWD}:/data" encryption-tool
```

## Running Tests

```bash
python -m unittest test_rsa -v
```

## Key Storage

Keep your `.key` and `.pem` files secure and do not commit them to version control. Add the following to your `.gitignore`:

```
*.key
*.pem
*.enc
*.henc
*.dec
*.hdec
*.bin
```
