import requests

payload = {'codes':100}
payload2 = {'username': 'maen', 'password':'2333'}

r = requests.get("https://httpbin.org/status",params=payload)
r2 = requests.post("https://httpbin.org/post",data=payload2) 

# print(r.url)
# print(r.text)
# print(r2.text)
# print(r2.url)
# print(r2.text)

# r_desc = r2.json()
# print(r_desc['form'])

r3 = requests.get("https://httpbin.org/basic-auth/maen/testing",auth=('maen','testing'))
print(r3.text)
