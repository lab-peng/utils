# pip install rsa
import rsa

(pubkey, privkey) = rsa.newkeys(1024)
msg = 'world of warcraft 魔兽世界'
byte_msg = msg.encode('utf-8')   # 字符串转换为字节 encode()
crypted_msg = rsa.encrypt(byte_msg, pubkey)
decrypted_msg = rsa.decrypt(crypted_msg, privkey)
signature = rsa.sign(byte_msg, privkey, 'SHA-1')



print(decrypted_msg)
print(decrypted_msg.decode()) # 字节转换为字符串 decode()


# print(signature)
invalid_signature = b'hello world'

try:
    rsa.verify(byte_msg, signature, pubkey)
    # rsa.verify(byte_msg, invalid_signature, pubkey)
    print('签名正确')
except rsa.pkcs1.VerificationError:
    print('签名错误')