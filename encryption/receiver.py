import json
import base64
import rsa
from cryptography.fernet import Fernet 

with open('pubkey.pem', 'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())
with open('privkey.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())
with open('payload.json') as fr:
    payload = json.load(fr)

# print(payload)

encrypted_symkey =  base64.b64decode(payload['encrypted_symkey'])
encrypted_data = base64.b64decode(payload['encrypted_data'])
signature = base64.b64decode(payload['signature'])

# decrypt encrypted_symkey back to symkey
symkey = rsa.decrypt(encrypted_symkey, privkey)
cipher = Fernet(symkey)

# decrypt data and verify signature
decrypted_data = cipher.decrypt(encrypted_data)

print(decrypted_data.decode())
try:
    rsa.verify(encrypted_symkey, signature, pubkey)
    # rsa.verify(encrypted_symkey, b'fake signature', pubkey)
    print('签名正确')
except rsa.pkcs1.VerificationError:
    print('签名错误')