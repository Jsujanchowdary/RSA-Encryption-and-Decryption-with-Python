# RSA Encryption and Decryption with Python

This repository demonstrates the implementation of RSA encryption and decryption using the PyCryptodome library in Python. The code uses RSA key generation, encryption with the public key, and decryption with the private key to ensure secure communication.

## Prerequisites

To run this project, you need to have Python installed along with the following dependencies:

- `pycryptodome` library

You can install it via pip:

```bash
pip install pycryptodome
```

## RSA Key Generation

RSA is an asymmetric cryptographic algorithm that uses a pair of keys:

- **Public Key**: Used to encrypt the message.
- **Private Key**: Used to decrypt the message.

This project demonstrates how to generate a pair of RSA keys, encrypt a message using the public key, and decrypt it using the private key.

## Code Walkthrough

### Key Generation

The RSA key pair is generated using the following code:

```python
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
```

Here, a 2048-bit RSA key pair is generated. The private key and public key are extracted for later use.

### RSA Encryption (Public Key)

Encryption is done using the `PKCS1_OAEP` cipher from the PyCryptodome library. The public key is used to encrypt the plaintext message:

```python
def rsa_encrypt(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(plaintext.encode())
    return encrypted
```

This function takes a plaintext string, encodes it to bytes, and returns the encrypted ciphertext.

### RSA Decryption (Private Key)

Decryption is performed using the private key and the `PKCS1_OAEP` cipher:

```python
def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()
```

This function takes the ciphertext, decrypts it, and returns the original message in string format.

### Example Usage

Here’s how you can use the encryption and decryption functions:

```python
message = "HELLO"
ciphertext = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(ciphertext, private_key)

print("RSA - Encrypted:", ciphertext)
print("RSA - Decrypted:", decrypted_message)
```

In this example, the plaintext message "HELLO" is encrypted with the public key, and the resulting ciphertext is then decrypted back to the original message using the private key.

## Output Example

When you run the example code, you will get the following output:

```text
RSA - Encrypted: b'...'  # The encrypted ciphertext (binary data)
RSA - Decrypted: HELLO
```

The encrypted ciphertext will be displayed as binary data, while the decrypted message will be the original plaintext ("HELLO").

## How to Run the Code

1. Clone the repository:

```bash
git clone https://github.com/Jsujanchowdary/RSA-Encryption-and-Decryption-with-Python.git
```

2. Navigate to the project directory:

```bash
cd RSA-Encryption-and-Decryption-with-Python
```

3. Run the script:

```bash
python rsa.py
```

## Conclusion

This project demonstrates basic RSA encryption and decryption in Python using the PyCryptodome library. It is an example of how asymmetric encryption works and can be used for secure data transmission.

---

### Example Directory Structure

```plaintext
rsa-encryption-python/
│
├── rsa.py     # Example script for RSA encryption/decryption
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```

---
