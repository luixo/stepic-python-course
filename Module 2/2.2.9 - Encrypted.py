from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
	
with open("passwords.txt", "rb") as inp:
	pwds = [s.decode("utf-8") for s in inp.read().split()]
	for pwd in pwds:
		try:
			print('Succesfully: ' + decrypt(pwd, encrypted).decode('utf8'))
		except:
			print('Password ' + pwd + ' didnt match')