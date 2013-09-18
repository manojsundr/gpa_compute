try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(**config)
import decimal
num_sems = raw_input("Number of semesters")
grades = {
}
response = str("y")
while response == "y":
	input = raw_input("Enter grade ")
	value = raw_input("Enter value ")
	grades[input] = value
	response = raw_input("Continue ? y/n ")
sem_sheet = {
}
units = 0
sem_cup = 0
total_points = 0
total_units = 0
for i in range(0,int(num_sems)):
	num_courses = raw_input("Enter number of courses for this sem ")
	for i in range(0,int(num_courses)):
		 grade = raw_input("Enter grade ")
		 unit  = raw_input("Enter the number of units of the course ")
		 units += int(unit)
		 for item in grades:
		 	if item == grade:
				sem_cup += int(unit)*int(grades[item])
	sem_sheet[sem_cup] = int(units)
for x in sem_sheet:
	total_points += x
	total_units += sem_sheet[x]
	x = round(decimal.Decimal(x/sem_sheet[x]),2)
cgpa = round(decimal.Decimal(total_points)/total_units,2)
i = 1
for x in sem_sheet:
	print "Semester "+ str(i) + ":" + str(x) + ":" + str(sem_sheet[x])
print cgpa 
