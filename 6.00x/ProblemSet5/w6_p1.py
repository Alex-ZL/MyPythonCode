def tryExercise():
	print "A",
	try:
		y = int("234")
		print "B",
	except ZeroDivisionError as e:
		print "C",
	else:
		print "D",
	finally:
		print "E",
	print "F"

tryExercise()
