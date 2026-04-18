# task 1 
# Takes student name and marks (0-100) as input and prints the grade (A, B, C, D, F) based on the following criteria:
# A: 80-100
# B: 70-79
# C: 60-69
# D: 50-59
# F: below 50
# Display name, marks and grade.

# name=input("Enter your name: ")
# marks=int(input("Enter your marks: "))
# grade=''
# if marks>=80:
#     grade='A'
# elif marks >=70 and marks <80:
#     grade='B'
# elif marks >=60 and marks <70:
#     grade='C'
# elif marks >=50 and marks <60:
#     grade='D'  
# else:
#     grade='F'

# def display():
#     print("Name: ",name)
#     print("marks: ",marks)
#     print("grade: ",grade)

# display()





# task 2

# write a program that takes a number from user .prints its multiple table up to 10 using a loop

# number=int(input("Enter a number: "))
# def table(num):
#     for i in range(1,11):
#         print(num,"x",i,"=",num*i)

# table(number)

# task 3
# Write a program that: 
# • Takes 10 numbers as input. Counts how many are even and odd. Displays the results. 

# even=0
# odd=0
# for i in range(10):
#     n=int(input(f"Enter the {i+1} number : "))
#     if n%2==0:
#         even=even+1
#     else:
#         odd=odd+1

# print(f"Even number are {even},odd number are{odd}")

# task 4

# Write a menu-driven program: 
# 1. Add element  
# 2. Remove element  
# 3. Display list  
# 4. Find maximum and minimum  
# • Use a list to store values.  
# • Perform operations based on user choice.  


# list=[]
# while True:
#     print("1Add element")
#     print("2Remove element")
#     print("3Display list")
#     print("4Find max and min")
#     print("5Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         element=int(input("Enter element to add: "))
#         list.append(element)
#     elif choice==2:
#         element=int(input("Enter element to remove: "))
#         if element in list:
#             list.remove(element)
#         else:
#             print("Element not found in list.")
#     elif choice==3:
#         print("List: ",list)
#     elif choice==4:
#         if len(list)>0:
#             print("Max: ",max(list))
#             print("Min: ",min(list))
#         else:
#             print("List is empty.")
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice please try again.")


# task 5


# write a program that 
# take a list of number (with duplicate )
# convert it into a set
# display unique element

# duplicateList = [1,2,3,4,4,5,5]
# newSet = set(duplicateList)

# print(newSet)


# task 6

 
# Create a class Student with: 
# • Attributes: name, roll_no, marks  
# • Methods:  
# o display() → shows student details  


# class student :
#     def __init__(self, name, roll, marks):
#         self.__name = name
#         self.__roll = roll
#         self.__marks = marks
    
#     def display(self):
#         print("Name:", self.__name)
#         print("Roll:", self.__roll)
#         print("Marks:", self.__marks)


# s=student("Ahmad",149,93)
# s.display()




# Task 7:  
# Create a class Rectangle: 
# • Attributes: length, width  
# • Methods:  
# o area()  
# o perimeter()


# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#     def  perimeter(self):
#         return 2 * (self.length + self.width)


# r =Rectangle(5,10)
# area=r.area()
# preimeter=r.perimeter()
# print(area)
# print(preimeter)





# Task 8: 
# Create a class BankAccount: 
# • Private attributes: balance  
# • Methods:  
# o deposit(amount)  
# o withdraw(amount)  
# o display_balance()  


# class BankAccount:
#     def __init__(self):
#         self.__balance=0
#     def deposit(self,amount):
#         self.__balance=self.__balance+amount
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance=self.__balance-amount
#         else:
#             print("current amount is greater than your balance")
#     def display(self):
#         print(f"Balance: {self.__balance}")


# b=BankAccount()
# deposit=b.deposit(5000)
# deposit=b.deposit(5000)
# withdraw=b.withdraw(4000)
# print(deposit)
# print(withdraw)
# b.display()
        

# Task 9: 

# Create: 
# • Base class Employee  
# • Derived class Manager  
# • Attributes: name, salary  
# • Method:  
# o calculate_bonus() (10% of salary for Employee, 20% of salary for 
# manager)

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def calculate_bonus(self):
#          return self.salary*0.10

# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary*0.20        
    
# e = Employee("Ibraheem", 50000)
# m = Manager("Ahmad", 80000)

# print(e.calculate_bonus())
# print(m.calculate_bonus())



# Task 10:  

# Use abc module: 
# • Abstract class Vehicle  
# • Abstract method start()  
# Derived classes: 
# • Car  
# • Bike

# from abc import ABC , abstractmethod

# class vehicle:
#     @abstractmethod
#     def start(self):
#         pass

# class car(vehicle):
#     def start(self):
#         print("Car start")

# class bike(vehicle):
#     def start(self):
#         print("bike start")

# c=car()
# c.start()
# b=bike()
# b.start()




# Task 11:
#  Create: 
# • Class Person  
# • Class Employee  
# • Class Manager (inherits from both)  
# Display combined details.


# class person:
#     def __init__(self,name):
#         self.name=name
    

# class employee:
#     def __init__(self,salary):
#         self.salary=salary

# class manager(person,employee):
#     def __init__(self,name,salary):
#         person.__init__(self,name)
#         employee.__init__(self,salary)

#     def display(self):
#         print(self.name,self.salary)


# m = manager("Ahmad Naveed",99999)
# m.display()
    


# Task 12: 
# Create a class Vector: 
# • Attributes: x, y  
# • Overload + operator to add two vectors 


# class vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         return vector(self.x+other.x,self.y+other.y)

# v= vector(1,2)        
# v1= vector(2,3)        

# final =v+v1

# print(final.x,final.y)


# taslk 13

# Write a program that: 
# • Takes 5 numbers and stores them in a tuple.  
# • Displays:  
# o Maximum value  
# o Minimum value  
# o Sum of elements  

# t = tuple(
#     int(input(f"Enter number {i+1}: ")) 
#     for i in range(5)
#     )

# print("Maximum:", max(t))
# print("Minimum:", min(t))
# print("Sum:", sum(t))



# Task 14:  
# Write a program that: 
# • Takes a sentence as input.  
# • Counts frequency of each word.  
# • Stores result in a dictionary.  
# • Displays word frequencies. 


# sen =input("Enter a sentence")
# words=sen.lower().split()

# freq={}

# for word in words:
#     if word in freq:
#         freq[word]=freq[word]+1
#     else:
#           freq[word]=1

# print("Words")
# for word ,count in freq.items():
#      print(word, count)


# Task 15:  
# Write a program that: 
# • Stores student names as keys and marks as values.  
# • Allows:  
# o Adding a student  
# o Updating marks  
# o Displaying all records 

# students = {}

# while True:
#     print("\n1.Add \n2.Update \n3.Display \n4.Exit")
#     ch = int(input("Choice: "))

#     if ch == 1:
#         name = input("name: ")
#         marks = int(input("marks: "))
#         students[name] = marks
#     elif ch == 2:
#         name = input("name: ")
#         students[name] = int(input("new marks: "))
#     elif ch == 3:
#         print(students)
#     else:
#         break


# Task 16:  
# Write a program that: 
# • Generates a random number (1–50).  
# • Asks the user to guess it.  
# • Provides hints:  
# o Too high  
# o Too low  
# • Ends when guessed correctly.  

# import random
# num=random.randint(1,20)
# while True:
#     guess=int(input("guess number"))
#     if guess>num:
#         print("high")
#     elif guess<num:
#         print("low")
#     else:
#         print("correct")
#         break




# Task 16(b):  
# Write a program that: 
# • Takes two lists from the user.  
# • Converts them into sets.  
# • Displays common elements.  



# list1 = input("Enter first list ").split()
# list2 = input("Enter second list").split()

# set1 = set(list1)
# set2 = set(list2)

# common = set1 and set2

# print("Common Elements:", common)



# Task 17:  
# Write a program that: 
# • Takes a string input.  
# • Checks whether it is a palindrome.  
# • Displays result.  



# Task 18:  
# Write a program that: 
# • Stores items and prices in a dictionary.  
# • Allows user to:  
# o Add items to cart (list)  
# o Calculate total bill  
# o Display cart items  


# items = {"apple": 50, "banana": 30, "milk": 100}
# cart = []

# while True:
#     item = input("Enter item or exit the system: ")
#     if item == "exit":
#         break
#     if item in items:
#         cart.append(item)

# total = sum(items[i] for i in cart)

# print("Cart:", cart)
# print("Total:", total)



# Task 19:  
# Write a program that: 
# • Takes a number as input.  
# • Checks whether it is prime or not. 


# num = int(input("Enter number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("invalid")


# Task 20:  
# Write a program that: 
# • Takes marks of n students.  
# • Stores in a list.  
# • Displays:  
# o Average marks  
# o Highest marks  
# o Lowest marks

n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    marks.append(int(input("Enter marks: ")))

print("Average:", sum(marks)/n)
print("Highest:", max(marks))
print("Lowest:", min(marks))