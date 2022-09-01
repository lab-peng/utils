# pip install rsa
# pip install cryptography
# https://www.youtube.com/watch?v=bd5nsMscPo0
# https://dianadarie.medium.com/jwt-authentication-with-sha-and-rsa-307e272f913f   # JWT for Django Rest Framework


# https://cryptography.io/en/latest/fernet/

# Fernet is built on top of a number of standard cryptographic primitives. Specifically it uses:

# AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.

# HMAC using SHA256 for authentication.

# Initialization vectors are generated using os.urandom().


import rsa
from cryptography.fernet import Fernet 


# generate keys and save rsa key pairs to files

# # We don't need to do this every day. Maybe update once in a while.
# (pubkey, privkey) = rsa.newkeys(2048)
# with open('pubkey.pem', 'wb') as f:
#     f.write(pubkey.save_pkcs1())

# with open('privkey.pem', 'wb') as f:
#     f.write(privkey.save_pkcs1())

key = Fernet.generate_key()  # generate a random key (symmetric key)
print(key)

# encrypt data and symmetric key
# sign it with a private key so we can verify it later
with open('data.json', 'rb') as f:
    data = f.read()

cipher = Fernet(key)
encrypted_data = cipher.encrypt(data)

with open('pubkey.pem', 'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())
with open('privkey.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())

encrypted_key = rsa.encrypt(key, pubkey)
signature = rsa.sign(encrypted_key, privkey, 'SHA-256')
# we can also sign with encryped_data with "signature = rsa.sign(encrypted_data, privkey, 'SHA-256')"
# but we have to verify the signature with "rsa.verify(encrypted_data, signature, pubkey)"

# decrypt and verify signature
decrypted_key = rsa.decrypt(encrypted_key, privkey)

decrypted_data = cipher.decrypt(encrypted_data)

<<<<<<< HEAD
print(decrypted_data.decode()[:100])
=======
# print(decrypted_data.decode())
>>>>>>> 92f2a14378145383740c5e48bbb65e995b9bbb93
try:
    rsa.verify(encrypted_key, signature, pubkey)
    # rsa.verify(encrypted_key, b'fake signature', pubkey)
    print('签名正确')
except rsa.pkcs1.VerificationError:
    print('签名错误')



