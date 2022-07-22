
# Python program showing a use
# of get() and set() method in
# normal function

class Student:
    def __init__(self, StdID, lastName, firstName, gpa, phoneNumber):
         self.StdID = StdID
         self.lastName = lastName
         self.firstName = firstName
         self.gpa = gpa
         self.phoneNumber = phoneNumber
    
    def __str__(self):
        return f'Student ID: {self.StdID}\nLast Name: {self.lastName}\nFirst Name: {self.firstName}\nGPA: {self.gpa}\nPhone Number: {self.phoneNumber}'
      
    # getter method
    def get_StdID(self):
        return self.StdID
    
    # getter method
    def get_lastName(self):
        return self.lastName

    # getter method
    def get_firstName(self):
        return self.firstName

    # getter method
    def get_gpa(self):
        return self.gpa

    # getter method
    def get_phoneNumber(self):
        return self.phoneNumber
      
    # setter method
    def set_stdID(self, x):
        self.StdID = x
    
     # getter method
    def set_lastName(self, x):
        self.lastName = x

    # getter method
    def set_firstName(self, x):
        self.firstName = x

    # getter method
    def set_gpa(self, x):
        self.gpa = x

    # getter method
    def set_phoneNumber(self, x):
        self.phoneNumber = x

countStudents = 0
totalGpa = 0
averageGpa = 0
slist = []
n = 1
print("Welcome to the Student Report System of Jumai B!")
print(n,"=========================================================.") 
n+=1
id = int(input("Please enter first student ID: "))
while True:

    if id != 0:
        lname = input("Please enter last name: ")
        fname = input("Please enter first name: ")
        gpa = float(input("Please enter GPA: "))
        num = input("Please enter phone number: ")
       

        std = Student(id, lname, fname, gpa, num)
       
        countStudents += 1
        totalGpa = totalGpa + gpa
        averageGpa = totalGpa / countStudents
        print("You just entered the following student record:")
        print(std)
        print("========= CURRENT REPORT OF ALL STUDENTS ===============")
        print("Current Student Count = ", countStudents)
        print("Total GPA of all students = ", totalGpa)
        print("Average GPA of all students = ", averageGpa)
        print("All student records are as follows:")
        slist.append([id, lname, fname, gpa, num])
        for i in range(len(slist)):
            print(slist[i])
        print("========= END OF REPORT =================================")
        print()
        print(n,"=========================================================.") 
        n+=1
        id = int(input("Please enter next student ID: "))
    else:
        print(n,"=========================================================.") 
        n+=1
        print("Thank you for using the Student Report System of Jumai B!")
        break
print(n,"=========================================================.") 
n+=1