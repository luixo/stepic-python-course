import sys, re

for line in sys.stdin:
	line = line.rstrip()
	if len(re.findall(r"\bcat\b", line)) > 0:
		print(line)