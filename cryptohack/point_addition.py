P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)
X = (5274, 2841)
Y = (8669, 740)

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
    
print(add(add(add(P, P), Q), R))