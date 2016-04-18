def closest_mod_5(x):
	return x if x % 5 == 0 else x + (5 - x % 5)
	
print(closest_mod_5(6))
print(closest_mod_5(7))
print(closest_mod_5(8))
print(closest_mod_5(9))
print(closest_mod_5(10))
print(closest_mod_5(11))