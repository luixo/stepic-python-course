from xml.etree import ElementTree

values = { 'red': 0, 'green': 0, 'blue': 0 }

def addValue(element, value):
	values[element.get('color')] += value
	for child in element:
		addValue(child, value + 1)

root = ElementTree.fromstring(input())
addValue(root, 1)
print(str(values['red']) + ' ' + str(values['green']) + ' ' + str(values['blue']))