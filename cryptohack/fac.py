def factor(n, e, d):
    """http://crypto.stackexchange.com/a/25910/17884
    
    n - modulus
    e - public exponent
    d - private exponent
    returns - (p, q) such that n = p*q
    """
    from math import gcd
    from random import randint

    while True:
        z = randint(2, n - 2)
        k, x = 0, e * d - 1

        while not x & 1:
            k += 1
            x >>= 1

        t = pow(z, x, n)
        if t == 1 or t == (n-1):
            continue

        bad_z = False
        for _ in range(k):
            u = pow(t, 2, n)

            if u == -1 % n:
                bad_z = True
                break

            if u == 1:
                p = gcd(n, t-1)
                q = gcd(n, t+1)
                assert n == p * q
                return p, q
            else:
                t = u

        if bad_z:
            continue