from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
import random
from math import gcd

p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)
e = []
d = []

for i in range(10):
    while True:
        tmp = random.randint(2, 65537)#phi - 1)
        if gcd(tmp, phi) == 1:
            e.append(tmp)
            d.append(pow(tmp, -1, phi))
            break

# Encrypt
m = b'Hello kitty!'
c = pow(bytes_to_long(m), e[1], n)
#print(long_to_bytes(pow(c, d[1], n)))

## Assum we only know e[0], d[0], and e[1]. We need to decrypt c.
k_tmp = (d[0] * e[0] - 1) // n
phi_new = 0

while True:
    if (d[0] * e[0] - 1) % k_tmp == 0:
        phi_new = (d[0] * e[0] - 1) // k_tmp
        break
    k_tmp += 1

d1 = pow(e[1], -1, phi_new)

print(long_to_bytes(pow(c, d1, n)))