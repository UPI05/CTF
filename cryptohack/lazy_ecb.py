p = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa76ade27a250155fce35ab24583edf387ce347b65ae4eea32cee7ac1304343468"

p1 = p[:32]
p3 = p[-32:]

res = ""

for i, j in zip(bytes.fromhex(p1), bytes.fromhex(p3)):
    res += "{:02x}".format(int(i) ^ int(j))

print(res)

print(bytes.fromhex("63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d"))