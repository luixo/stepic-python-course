try:
    foo()
except AssertionError as e:
	print("AssertionError")
except ZeroDivisionError as e:
	print("ZeroDivisionError")
except ArithmeticError as e:
	print("ArithmeticError")