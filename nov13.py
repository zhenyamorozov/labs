import json
t = [1,2,3, {'key': "value", 'yesno': True}]
st = json.dumps(t)

print(t)
print(st)