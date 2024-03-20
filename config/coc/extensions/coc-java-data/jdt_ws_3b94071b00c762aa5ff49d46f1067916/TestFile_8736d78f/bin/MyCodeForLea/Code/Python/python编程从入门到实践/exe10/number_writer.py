import json

number = [2,3,5,7,11,13]
filename = 'number.json'

with open(filename,'w') as f:
    json.dump(number,f)
