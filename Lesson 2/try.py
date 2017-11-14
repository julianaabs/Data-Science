numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
	try:
		int('')
	except Exception:
		print("There was an error")
