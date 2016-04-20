with open('dataset_24465_4.txt') as f, open('2.4.4 - Filesystem - RESULT.txt', 'w') as w:
	w.write("".join(list(reversed(f.readlines()))))