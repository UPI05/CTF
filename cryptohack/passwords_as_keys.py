c = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

from Crypto.Cipher import AES
import hashlib
import random

with open('../../words.txt') as f:
    words = [w.strip() for w in f.readlines()]


ciphertext = bytes.fromhex(c)

for word in words:
    key = hashlib.md5(word.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
        if (b'crypto' in decrypted):
            print(decrypted)
            exit(0)
    except ValueError as e:
        print({"error": str(e)})