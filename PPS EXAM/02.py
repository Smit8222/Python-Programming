# Q.1
'''num = int(input("Enter your no of which factorial to be find :"))
fact = 1
i = 1
while i<= num:
    fact = fact * i
    i = i + 1
print("foctorial of give number is :",fact )'''


# Q.2
'''num = 0
i = 1
while i<= 5 :
    num = num + i
    i = i + 1
print("sum =",num)   ''' 

'''fruit = ["apple","banana","cherry"]
for i in fruit :
    print(i)'''

'''for i in range(0,5):
    print("smit")'''

'''for i in range(1,6):
    print(i)'''

'''sum = 0
for i in range(1, 11):
    sum = sum + i
print("THE sum of 1 to 10 no. is :" , sum)    '''

'''num = int(input("Enter the number of term or elements upto which fibonacci siries is to be produce ="))
a = 0
b = 1
print("fibonacci series is = ")
print(a)
print(b)
i = 3
while i <= num:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1'''

'''for i in range(1, 6):
    for j in range(1, i +1):
        print("👻", end = "  ")
    print("  ")    '''

'''for i in range(6, 1,-1):
    for j in range(i , ):
        print("*",end=" ")
    print(" ")    
    '''

'''print("Q.1","UNIT 5","(PPA)")
class student:
    school = "ABC school"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

s1 = student("smit", 101)
s2 =student("ridhi",102)

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)


student.school
print(s1.school)'''
        
'''class employee:
    def __init__(self):
        self.name = "name"
        self.__salary = "salary"

def set_salary(self):
    return self.__salary

def set_salary(self, salary):
    if salary > 0:
        self.__salary = salary
    else:
        print("Invaild salary!")

def display(self):
    print(f"Name: {self.name}, salary : {self.__salary}")

emp = employee("Amit",50000)
print(emp._salary())
emp.set_salary(60000)
emp.display() '''

'''square = lambda x : x * x
print(square(5))'''

'''import math
print(type(math.sqrt(25)))
print((math.sqrt(25)))

'''
for i in range(1,11):
    print("Table of",i)
    for j in range(1,11):
        print(i*j)