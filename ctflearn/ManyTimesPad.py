def solve(data):
    while(True):
        flag = input('Flag: ')
        dt = data.copy()
        for i in range(len(dt)):
            st = ""
            for j in range(min(len(flag), len(dt[i]))):
                st += chr(ord(flag[j]) ^ ord(dt[i][j]))
            dt[i] = st
        for i in range(len(dt)):
            print(i, end='')
            print('.', end='')
            print(dt[i])
        line = int(input('Line: '))
        ch = input('Character: ')
        print('New flag: ' + flag + chr(ord(ch) ^ ord(data[line][len(flag)])))

with open('msg') as f:
    solve([bytes.fromhex(x).decode('utf-8') for x in f])
