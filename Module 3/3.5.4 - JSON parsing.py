import json

def getParentByName(parentName):
	for clazz in data:
		if clazz['name'] == parentName:
			return clazz
	return None
	
def findChildren(parent):
	children = set()
	for child in parent['children']:
		children.add(child)
		children = children.union(findChildren(getParentByName(child)))
	return children
	
data = json.loads(input())
for child in data:
	child['children'] = set()
for child in data:
	for parentName in child['parents']:
		parent = list(filter(lambda x: x['name'] == parentName, data))[0]
		parent['children'].add(child['name'])

for child in sorted(map(lambda x: x['name'] + ' : ' + str(len(findChildren(x)) + 1), data)):
	print(child)