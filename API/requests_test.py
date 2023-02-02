import requests

url = 'https://xkcd.com/353/'
r = requests.get(url)
#print(dir(r))

print(r.status_code)
print(r.headers)
with open('comic.jpg', 'wb') as f:
    f.write(r.content)


payload = {'page': 2, 'count': 25}
r1 = requests.get('https://httpbin.org/get', params=payload)
#print(r1.headers)
print(r1.text)
print(r1.url)

payload = {'username': 'sush', 'password': 'test'}
r2 = requests.post('https://httpbin.org/post', data=payload)
print(r2.text)

