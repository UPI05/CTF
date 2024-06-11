from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)

m = b'Send me 5 billion dollars'
s = pow(bytes_to_long(m), d, n)


# Assum that the system doesn't sign the message m, so the attacker has to send m' that is different from m to find out the signature for m

x = 2

m2 = (pow(x, e, n) * bytes_to_long(m)) % n
s2 = pow(m2, d, n)

s3 = (s2 * pow(x, -1, n)) % n

print(s3 == s)
