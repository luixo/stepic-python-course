objects = objects if 'objects' in locals() else [1, 2, 1, 2, 3]
num = 0
sortedObjects = sorted(objects, key=id)
for key, obj in enumerate(sortedObjects):
	if key == 0 or not obj is sortedObjects[key - 1]:
		num += 1
print(num)