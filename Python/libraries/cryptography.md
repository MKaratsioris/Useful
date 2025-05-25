- Install
$ pip install cryptography

- Use
from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Move the key to a variable
k = Fernet(key)

plaintext = b"This is a plaintext"

# Encrypt
ciphertext = k.encrypt(plaintext)
print(ciphertext)

# Decrypt
decrypted_text = k.decrypt(ciphertext)
print(decrypted_text)