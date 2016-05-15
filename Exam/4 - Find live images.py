import requests, re, sys

file = input()
linkRE = r"<img[^>]*\ssrc=['\"](.*?)['\"]"

res = requests.get(file)
good = 0
for image in re.findall(linkRE, res.text):
	img = requests.get(image)
	if img.headers['content-type'].startswith('image') and img.status_code == 200:
		good += 1
print(good)