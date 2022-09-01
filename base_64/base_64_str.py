import base64

string = '342427197910022238'

encoded = base64.b64encode(string.encode())
print(encoded, type(encoded))

print(str(encoded)[2:-1])

