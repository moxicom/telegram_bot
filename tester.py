import json

f = open('items.json')
json_string = f.read()
json_data = json.loads(json_string)
items = list(json_data)
f.close()
items.append('keeek')
print(items)
f = open('items.json', 'w')
json.dump(items, f, indent=4)



