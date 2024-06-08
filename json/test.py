import json
import os
from pathlib import Path

print("============== output ====================")
# people = '''
# {
#     "people":[
#         {
#             "name":"maen mohammad",
#             "phone":"0798888282",
#             "email":"maen@maen.con",
#             "has_license":false,
#             "age":43
#         },
#         {
#             "name":"tyma maen mohammad",
#             "phone":"078999982",
#             "email":"tyma@tyma.con",
#             "has_license":false,
#             "age":1
#         }
#     ]
# }
# '''

# data = json.loads(people)

# for person in  data["people"]:
#   print(person['name'])
#   del person['phone']

# string = json.dumps(data,indent=2,sort_keys=True)

# print(string)

# ==================================
# ========== load json file ========
# ==================================


path = os.path.join(os.getcwd(), 'json/counties.json')

with open(path) as f:
    data = json.load(f)

string = json.dumps(data,indent=2)
print(string)

with open('json/new_counties.json', 'w') as f:
    json.dump(data,f)
    
