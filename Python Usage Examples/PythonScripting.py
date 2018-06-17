import json
with open('input.json', 'r') as input:
        obj = json.load(input)  # type: object
        print('Hello, ' + obj['name'])
