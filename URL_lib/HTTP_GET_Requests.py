from urllib.request import urlopen
import json

print("========================================")

url = "https://jsonplaceholder.typicode.com/todos/1"

with urlopen(url) as response:
     body = response.read()


todo_item = json.loads(body)


# new example 

with urlopen("https://www.example.com") as response:
     print(response.getheader('Server'))

print("========================================")
