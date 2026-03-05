#CODE ALONG: Create a minion class with several attributes - some that are the same 
#for every minion, and some that are different. 
#Create an instance of the class (an object!) and print it to the console.
#The above is the work we did in class, just copy paste it for reference.





#If time permits, continue adding attributes after the whole class portion is done.
#Otherwise, remember you must at least finish the mild task below.


#YOUR TASK: Complete the following to the best of your ability. Thank you to
#			Ms. Shuman for her example tasks!
#MILD 🌶

#1. Create a class called Student that has two attributes: a name, and a grade.

class Student:
    def __init__(self,theName,theGrade):
        self.name = theName
        self.grade = theGrade

# Now create instances of three different students (student1, student2, and student3).
student1 = Student("Tom", 11)
student2 = Student("John", 12)
student3 = Student("Bob", 10)


#Confirm that the class works by printing out the first student's name.

print(student1.name, student1.grade) 


# MEDIUM 🌶🌶

#2. Create a class called School that has three attributes: a name, a type, and
#	a size (number of students).

class School:
    def __init__(self, theName, theType, theSize):
        self.name = theName
        self.type = theType
        self.size = theSize
        

#Create instances of three individual schools.

school1 = School("Stuyvesant", "High School", 4000)
school2 = School("Francis Lewis", "High School", 4000)
school3 = School("Brooklyn Tech", "High School", 5000)

#Confirm that the class works by printing out the name and size of the third school.
print(school3.name, school3.size)


###
#3. Create a class called House that has four attributes: an address, a number
#	of bathrooms, a price, and a number of bedrooms.

class House:
    def __init__(self, add, br, cost, bd):
        self.address = add
        self.bathrooms = br
        self.price = cost
        self.bedrooms = bd

#Create instances of at least three individual houses.
house1 = House("1092 12 Ave", 2, 400000,5)
house2 = House("1298 10 Ave", 4, 1011001, 6)
house3 = House("0212 102 St", 1, 21912, 2)


#Confirm that the class works by printing out the address and size of the second house.

print(house2.address, house2.bedrooms, house2.bathrooms)

#SPICY 🌶🌶🌶

#4. Put your three students in a list called my_students, your houses in a list
#	for houses, and your schools in a list for schools.

my_students = [student1, student2, student3]
houses = [house1, house2, house3]
schools = [school1, school2, school3]

#Iterate (this means use a loop!) over the student list, printing out "_____ is in
#grade __." For each of the students.

for student in my_students:
    print(student.name , " is in grade " , student.grade) 

#Iterate over the houses list and print out a description for each one. Do the same
#for your schools lists.

for house in houses:
    print("Address: " , house.address , ", " , "Bedroom: " , house.bedrooms, ", " , "Bathrooms: " , house.bathrooms, ", ", "Cost: $", house.price)

for school in schools:
    print(school.name, school.type, ": ", school.size)
###
#5. Modify your student class above to include a savings_account value for each
#	student. Change your initializers so that the code still runs. 



#Write some code that compares a student and a house, and determines whether or not
#the student can afford to buy the house. 