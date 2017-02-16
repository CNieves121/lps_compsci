class Student(object):
	""" Encapsulates a Student, their gpa and college app list. """
	
	def __init__(self, name, gpa, fav_snack):
		self.name = name
		self.gpa = gpa
		self.fav_snack = fav_snack

		self.collegelist = []

	def getSnack(self):
		return self.fav_snack

class College(object):
	"""Encapsulates a school."""
	
	def __init__(self, name, minGPA):
		self.name = name
		self.minGPA = minGPA
	def acceptStudent(self, studentGPA):
		if studentGPA > self.minGPA:
			return(True)
		else:
			return(False)


#code execution starts here
myFirstChoice = College("Columbia", 3.95)
KrystalGPA = 4.0
print("Did Krystal get in?")
print(myFirstChoice.acceptStudent(KrystalGPA))







myFirstStudent = Student("Jenny", 4.0,"Carrots")
print(myFirstStudent.getSnack())

mySecondStudent = Student("Kelvin", 3.0,"Takis")
print(mySecondStudent.getSnack())
