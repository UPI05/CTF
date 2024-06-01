first_block = b"admin=False;expi"
fake_first_block = b"admin=True;;expi"

c = "2e002ece3ab252e06ef1950c7e8c04c3dfb678bdd90dd75c5ddf4c7bc58473062a6fab9adcff17628959d310831efcef"

iv = c[:32]
cookie = c[32:]

p1 = ""

for i, j in zip(first_block, bytes.fromhex(iv)):
    p1 += "{:02x}".format(int(i) ^ int(j))

fake_iv = ""

for i, j in zip(fake_first_block, bytes.fromhex(p1)):
    fake_iv += "{:02x}".format(int(i) ^ int(j))

print(fake_iv)
print(len(fake_iv))
print(cookie)
print(len(cookie))