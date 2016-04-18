namespaces = { 'global': { 'parent': None, 'vars': [] } }
for i in range(0, int(input())):
	command = input().split()
	if command[0] == 'create':
		if namespaces.get(command[1]) == None:
			namespaces[command[1]] = { 'parent' : command[2], 'vars': [] }
	elif command[0] == 'add':
		if not namespaces.get(command[1]) == None:
			namespaces[command[1]]['vars'].append(command[2])
	else:
		if not namespaces.get(command[1]) == None:
			namespace = command[1]
			res = None
			while res == None and not namespace == None:
				res = namespace if command[2] in namespaces[namespace]['vars'] else None
				namespace = namespaces[namespace]['parent']
			print(res)