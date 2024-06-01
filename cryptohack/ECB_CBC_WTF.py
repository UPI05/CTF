c = "3a4b66fa48a1ea384af72bfc870c12d01f25ee5b3e0a985c4a5d5f63498904f032e65a83110736f71334ae444963337d"
iv = c[:32]
block1 = c[32:64]
block2 = c[64:]

print(iv)
print(block1)
print(block2)

block1_decrypted = "59391f8a3cce910b299574c9f26f79e5"
block2_decrypted = "4011986b0f6ec76d7d027e4268a8258d"

for bytei, bytej in zip(bytes.fromhex(block1_decrypted), bytes.fromhex(iv)):
    print(chr(bytei ^ bytej), end='')

for bytei, bytej in zip(bytes.fromhex(block1), bytes.fromhex(block2_decrypted)):
    print(chr(bytei ^ bytej), end='')

