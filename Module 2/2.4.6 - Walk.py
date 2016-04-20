import os.path

with open('2.4.6 - Walk - RESULT.txt', 'w') as f:
	f.write("\n".join(sorted([dir.replace('\\', '/').replace('./main', 'main') for dir, _, dirfiles in os.walk('./main') if len([file for file in dirfiles if os.path.splitext(file)[1] == '.py']) > 0])))