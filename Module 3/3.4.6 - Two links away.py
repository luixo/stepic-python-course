import requests, re

fr = input()
to = input()
linkRE = r"<a href=['\"]([\w/:\.]+)['\"]"

res = requests.get(fr)
links = re.findall(linkRE, res.text)
for link in links:
	res = requests.get(link)
	links = re.findall(linkRE, res.text)
	if to in links:
		print("Yes")
		break
else:
	print("No")