# 🔒 Security and Cryptography: Protecting Your Data

import hashlib
import secrets

# 1. Hashing Passwords (One-way)
# We store 'hashes' so even if database leaks, we don't leak passwords!
# Use SHA-256 (Very common for security)
password = "my_secure_password"
# Combine with a 'salt' to prevent pre-computed attacks (Rainbow Tables)
salt = secrets.token_hex(8)
pass_plus_salt = password + salt

# SHA-256 Hashing
hashed_pass = hashlib.sha256(pass_plus_salt.encode()).hexdigest()
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_pass}")

# To verify: Hash the provided password with the stored salt...
# ...if hashes match, password is correct!

# 2. Generating Safe Secrets (Like API Keys or Tokens)
# secrets module is more secure than 'random' for security tasks!
api_key = secrets.token_urlsafe(16)
print(f"Generated API Key: {api_key}")

# 3. Comparing Secrets safely (Prevents timing attacks!)
# secrets.compare_digest(stored_key, provided_key)
# if secrets.compare_digest(api_key, provided_key):
#     print("Access Granted!")

# 4. Built-in Cryptography?
# Python's standard library is mostly about hashing.
# For encryption (AES/RSA), you usually use 'cryptography' library:
# pip install cryptography

# Summary Table
"""
| Module         | Purpose                                         |
|----------------|-------------------------------------------------|
| hashlib        | SHA-256, MD5, SHA-512 Hashing (Passwords/Data)  |
| secrets        | Cryptographically strong random numbers/tokens  |
| hmac           | Checking if data was tampered with in transit   |
| ssl            | Secure sockets (HTTPS-like connections)         |
| base64         | Converting binary data to text (to send/save)   |
"""
