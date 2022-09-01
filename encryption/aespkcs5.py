# pip install aes-pkcs5

import base64
from aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


# # generate keys and save rsa key pairs to files, we don't need to do this every day. Maybe update once in a while.
# (pubkey, privkey) = rsa.newkeys(2048)
# with open('pubkey.pem', 'wb') as f:
#     f.write(pubkey.save_pkcs1())

# with open('privkey.pem', 'wb') as f:
#     f.write(privkey.save_pkcs1())

key = '7SVHzk9KEUntynnU'
output_format = "b64"
print(key)

# encrypt data with symmetric key
# sign it with a private key so we can verify it later
with open('data.json', encoding='utf-8') as f:
    data = f.read()

# # cipher = Fernet(key)
cipher = AESECBPKCS5Padding(key, output_format)
print(type(data))
encrypted_data = cipher.encrypt(data)
# print(encrypted_data)

# with open('pubkey.pem', 'rb') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read())
# with open('privkey.pem', 'rb') as f:
#     privkey = rsa.PrivateKey.load_pkcs1(f.read())

# 评估公司公钥（PEM格式）
pubkey = RSA.import_key("""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArzotSdangChzIbK2XVSc
U67NK8NYDVjmRlesyzf4yBVE/s9ECpxCc7aVck/uzt1vFKDCDbPF508pyXKiK1ft
aOXb1lmHo+Med1N/mwY2v1/4yMJe39taK6eDaMd625XyaWrk2fEn+C02sz9mLLg6
emd1SSftnjFGpZ86cCP7H7dY81tMyT2UFHjrSHcgWRYihWCSQfcLqrlHz1PvM6Am
X2nUo6VVWjKxoZbHlMlsEpBntlJpHVOvYdmpklwYFYo8Ko917csPxtKryeuGcoAO
NONdUB1kGU7XjuHsMEsW3+1fCmtuLJ5tNepWOE9Ynf7ZGzo3XK3a20ShNUr9x7L5
9QIDAQAB
-----END PUBLIC KEY-----""")

# 评估公司私钥（PEM PKCS1格式）PEM PKCS8格式也可
privkey = RSA.import_key('''-----BEGIN PRIVATE KEY-----
MIIEogIBAAKCAQEArzotSdangChzIbK2XVScU67NK8NYDVjmRlesyzf4yBVE/s9E
CpxCc7aVck/uzt1vFKDCDbPF508pyXKiK1ftaOXb1lmHo+Med1N/mwY2v1/4yMJe
39taK6eDaMd625XyaWrk2fEn+C02sz9mLLg6emd1SSftnjFGpZ86cCP7H7dY81tM
yT2UFHjrSHcgWRYihWCSQfcLqrlHz1PvM6AmX2nUo6VVWjKxoZbHlMlsEpBntlJp
HVOvYdmpklwYFYo8Ko917csPxtKryeuGcoAONONdUB1kGU7XjuHsMEsW3+1fCmtu
LJ5tNepWOE9Ynf7ZGzo3XK3a20ShNUr9x7L59QIDAQABAoIBAFinAWS7IjF3xZAF
/7fGZ/T6mjkK8tCF6rMqBnUmU0q/YBHewRjxJ7mtZXzZLgQhCeMQ1jzieDzn00dl
JODy8l1A9fFDiJmE/dP3Pbcr9KTsJE1F8YQmUT+G17g6PFE+Us+80h3loYgxL9yO
Nd5oMsXc8/zYI6MGYSzIG2PDAHlxjiOM/9MqsZlNiCeYJQsoY8ohEIfLbe0FzR9f
dmkqFzwCVL/NC98mLSdXeOt29MkZMYFEI6uVnFZObiCLmJ0aWsJLpkKXzC0oTvjP
KY5v1ij505vCwuDa7KlIbhw9yG/oqv4kSDhzAo0YzmJEgBWAzOR69plRVvPN6Cbv
MjydhR0CgYEA3L00oJO3yXWELWsErNcdgMewrPz30Wj/gpG/UZfYa2g46DbVw2aY
sGHbrZ8ZTuQykmRrYbOh6TyzWqgCIPJ8pZVOaSOsYz7IErpjioX9gzkG8QK9K5q+
Xl1GOpA85of6BygaC2xvc2+QJA5REu0sBv2dPcDHw/DfMsYNan0P36sCgYEAyzfV
SM1LgjcCYX/mJp0NdonxcMFfUsZPYkQF3d0/w2Fq9oXb20RmW5obMWiNSIiB7mi8
WT+LTzLNSJmX8nPj+03bNyjem7FOOUhe+dG1Nc8WhJRrkrck6wc+QsmOR7WOqBL+
5rO2aiqS5t6rasoSUlddv5mhHAKgFEmFglaJbN8CgYBpzBmUORimaze92QQ1nyjZ
11v7nYddjBiiyR5Mih3FZP+ZdObBr8PRDiYPMikcIc2HUrAQ9NrOgjRoaAwVJIPP
jR82z01JiAa2yzT4aL4YDdYg37IxWwqRCd2mJgm6aEPS+Ep7XS6Rwk/wqBf9nUUz
2Ixr06ErbaBcooY9mtFn3wKBgFg/ytNus5e8o8ALdrrWAP61MLAyiV6818RondOX
PRVvvK+JucwijADDj4OJT7Fr9mC+Au0O90RRX2xjpuSXBy4exU/S47jg6oNdtkDu
nK7dW33/pid0eQfHgXYnaS4i3eyHM0KkUFcSXfD8SZx6XDJ91ixaXuh3C2VD+EJ9
qfgpAoGAN0M++ltJ/uXcqst+zejIDtHpjiG3UsDwn43JGw+u1ofkp50jpDrm5i7Q
5+zuvRBND9i/YDh7cUMjrb0epF+BnYqMW0fF5CS8eVFTxzl5tBOWlg+Q3Xc2MZF1
HcOAp3qSItTgtXt3H5Nld2+dRDikeTJg0V5Vd7aifCpLDmzcnvM=
-----END PRIVATE KEY-----''')



# we can also sign with encryped_data with "signature = rsa.sign(encrypted_data, privkey, 'SHA-256')"
# and then verify the signature with "rsa.verify(encrypted_data, signature, pubkey)"
signer = PKCS1_v1_5.new(privkey)
h = SHA256.new(encrypted_data.encode())
signature = base64.b64encode(signer.sign(h))
print(signature)

# decrypt and verify signature
h = SHA256.new(encrypted_data.encode())
verifier = PKCS1_v1_5.new(pubkey)
print(verifier.verify(h, base64.b64decode(signature)))  # bool value 


decrypted_data = cipher.decrypt(encrypted_data)

# print(decrypted_data)
# try:
#     rsa.verify(encrypted_key, signature, pubkey)
#     # rsa.verify(encrypted_key, b'fake signature', pubkey)
#     print('签名正确')
# except rsa.pkcs1.VerificationError:
#     print('签名错误')




























# # b64
# key = "@NcRfUjXn2r5u8x/"
# output_format = "b64"
# message = '''
# [
#     {
#         "报告编号": "测绘收费(2020)第00001号",
#         "项目类型": "测绘类",
#         "委托方": "苏州市自然资源和规划局吴中分局",
#         "委托方电话": "111",
#         "项目坐落": "11",
#         "所属区域": "苏州-园区",
#         "估价目的": "流转",
#         "宗地用途": "商业",
#         "接件时间": "2020-04-01",
#         "评估人员": "孙以山",
#         "项目收费情况": "已开票收费",
#         "项目状态": "待查勘",
#         "房产单价": null,
#         "土地单价": null,
#         "房产总价": null,
#         "土地总价": null,
#         "评估金额": null,
#         "开票总金额": 140805.0,
#         "收费总金额": 140805.0,
#         "估价时点": "2020-03-31",
#         "编号类型": "测绘收费",
#         "项目性质": "线下",
#         "土地面积": 11.0,
#         "房产面积": 11.0,
#         "其中阁楼面积": null,
#         "其中地下室面积": null,
#         "物业类型": "普通多层",
#         "产证类型": "《不动产权证》",
#         "项目负责人": "公司",
#         "权利人": "11",
#         "资产估价师": null,
#         "土地估价师": null,
#         "房产估价师": "沈勇,应丽平",
#         "总层数": 1.0,
#         "层数": "1",
#         "特殊计件": "否",
#         "土地使用权类型": "划拨",
#         "竣工日期": 2020,
#         "终止日期": null,
#         "项目备注信息": null
#     }
# ]
# '''

# cipher = AESECBPKCS5Padding(key, output_format)
# encrypted = cipher.encrypt(message)
# # print(encrypted)
# # assert encrypted == "Woij9gRapIm0Z9DyDPiRqs4k30gO+/Q+BfHhpGzXuXCP7Siu22r178EBGHZ4BBJl"
# assert cipher.decrypt(encrypted) == message

