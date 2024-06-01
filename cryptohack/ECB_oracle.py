alphabet_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]
special_characters = list("{}_!@#$%^&*()-=+[]|;:'\",.<>?/`~")
alphabet_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
all_characters = alphabet_lower + alphabet_upper + digits + special_characters

import requests
import json

url = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'
'''
# Found flag_len = 25 bytes
u = url
cnt = 0
flag_len = 0

while True:
    cnt += 1
    u = u + 'aa'
    print(u)
    l = len(json.loads(requests.get(u).text)["ciphertext"])
    if l > 64:
        flag_len = 32 - cnt # bytes
        break

'''

def check(u1, u2, len1=32, len2=32):
    return json.loads(requests.get(u1).text)["ciphertext"][:len1] == json.loads(requests.get(u2).text)["ciphertext"][:len2]

def check2(u1, u2):
    return json.loads(requests.get(u1).text)["ciphertext"][64:96] == json.loads(requests.get(u2).text)["ciphertext"][64:96]


flag_prefix = ""

for i in range(1, 16):
    u = url + "aa"* (16 - i)
    ok = False
    for c in all_characters:
        u2 = u + flag_prefix + "{:x}".format(ord(c))
        if check(u, u2):
            flag_prefix += "{:x}".format(ord(c))
            ok = True
            break
    if not ok:
        print("ERR")
        exit(1)
    else:
        print("found: ", bytes.fromhex(flag_prefix))


flag_postfix = ""


for i in range(1, 16):
    u = url + "aa" * (32 - (25 - i))
    ok = False
    for c in all_characters:
        u2 = url + "aa" * 32 + "{:x}".format(ord(c)) + flag_postfix + ("{:02x}".format(int(15 - len(flag_postfix) / 2 ))) * int(15 - len(flag_postfix) / 2 )
        if check2(u, u2):
            flag_postfix = "{:x}".format(ord(c)) + flag_postfix
            ok = True
            break

    if not ok:
        print("ERR")
        exit(1)
    else:
        print("found: ", bytes.fromhex(flag_postfix))



# crypto{p3n6u1n5_h473_3cb}