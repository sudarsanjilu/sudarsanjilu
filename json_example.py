import json

# JSON String:
colors = '["Red", "Yellow", "Green", "Blue"]'

# JSON string to python list:
lst1 = json.loads(colors)
print(lst1)

list2 = ['Red','green','yellow','blue']
jsonObj = json.dumps(list2)
print(jsonObj)
