import requests, re, sys

file = input()
linkRE = r"<a [^>]*\s*href=['\"](?!\.\./)(?:\w+://)?([\w\.-]+)(?:.*)['\"]"

res = requests.get(file)
print("\n".join(sorted(list(set(re.findall(linkRE, res.text))))))