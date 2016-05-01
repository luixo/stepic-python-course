import requests, json

with open('numbers.txt') as file:
	for line in file:
		if (json.loads(requests.get('http://numbersapi.com/' + line.rstrip() + '/math?json=true').text)['found']):
			print("Interesting")
		else:
			print("Boring")