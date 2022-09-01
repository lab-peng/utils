import json
import base64 
import rsa
from cryptography.fernet import Fernet 

# generate a random key (symmetric key)
symkey = Fernet.generate_key()  
print(symkey)

# encrypt data and symmetric key
# sign it with a private key so we can verify it later
with open('data.json', 'rb') as f:
    data = f.read()

cipher = Fernet(symkey)
encrypted_data = cipher.encrypt(data)

with open('pubkey.pem', 'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())
with open('privkey.pem', 'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())

encrypted_symkey = rsa.encrypt(symkey, pubkey)

# sign with privkey
signature = rsa.sign(encrypted_symkey, privkey, 'SHA-1')

# print(encrypted_symkey, type(encrypted_symkey))
# print(base64.b64encode(encrypted_symkey).decode('utf-8'), type(base64.b64encode(encrypted_symkey).decode('utf-8')))


payload = {
    'encrypted_symkey': base64.b64encode(encrypted_symkey).decode('utf-8'),
    'encrypted_data': base64.b64encode(encrypted_data).decode('utf-8'),
    'signature': base64.b64encode(signature).decode('utf-8'),
}

# send the json message to receiver
with open('payload.json', 'w') as f:
    json.dump(payload, f, indent=4)

