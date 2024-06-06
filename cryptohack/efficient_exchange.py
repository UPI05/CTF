
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

G = (1804, 5368)
a = 497
b = 1768
p = 9739

def extended_euclid(a, b):
    xa, ya = 1, 0
    xb, yb = 0, 1

    while b != 0:
        q = int(a // b)
        r = a % b
        a = b
        b = r
        xr = xa - q * xb
        yr = ya - q * yb
        xa, ya = xb, yb
        xb, yb = xr, yr
    
    return (xa, ya)


def rev_mod(a, m):
    return (extended_euclid(a, m)[0] % m + m) % m


def add(u, v):
    if u[0] == u[1] and u[0] == 0:
        return v
    elif v[0] == v[1] and v[0] == 0:
        return u
    elif u[0] == v[0] and u[1] == -v[1]:
        return (0, 0)
    else:
        if u == v:
            ld = (((3 * ((u[0] ** 2) % p)) % p + a) % p) * (rev_mod(2 * u[1], p) % p) % p
        else:
            ld = (((v[1] - u[1]) % p) * (rev_mod(v[0] - u[0], p) % p)) % p

        print(ld)
        x3 = (((ld ** 2) % p) - u[0] - v[0]) % p
        x3 = (x3 + p) % p
        return (x3, (((((ld * (u[0] - x3)) % p) - u[1]) % p) + p) % p)
    

def smul(n, P):
    Q = P
    R = (0, 0)

    while n > 0:
        if n % 2:
            R = add(R, Q)
        
        Q = add(Q, Q)
        n = n // 2
    
    return R

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

def sqrt(y2, p):
    for i in range(p):
        if (i * i) % p == y2:
            return i
    return -1

x = 4726
n = 6534

y2 = (((x ** 3) % p) + ((497 * x) % p) + 1768 % p) % p

y = sqrt(y2, p)

Q1 = (x, y)
Q2 = (x, -y + p)

obj = {'iv': 'cd9da9f1c60925922377ea952afc212c', 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}
shared_secret = smul(n, Q1)[0]
iv = obj['iv']
ciphertext = obj['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))
