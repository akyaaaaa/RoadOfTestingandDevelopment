import requests
# r = requests.post('http://httpbin.org/post',data={'name':'liu'})
r = requests.get('https://api.github.com/events')
print(r.json())
