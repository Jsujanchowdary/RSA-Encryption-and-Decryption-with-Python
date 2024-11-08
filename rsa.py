from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Encrypt
def rsa_encrypt(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(plaintext.encode())
    return encrypted

# Decrypt
def rsa_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.decode()

# Example usage:
message = "HELLO"
ciphertext = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(ciphertext, private_key)
print("RSA - Encrypted:", ciphertext)
print("RSA - Decrypted:", decrypted_message)
