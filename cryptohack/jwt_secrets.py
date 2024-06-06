import jwt

encoded = jwt.encode({'username': "upi05", 'admin': True}, "secret", algorithm='HS256')

print(encoded)