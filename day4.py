'''
if statement ---> this (if statement) is used to check any condition, if the condition bacomes true it will enter in side the(if statement)
age = int(input ("Enter your age:"))
if age >=18:
print ("your age is 18 or above")'''
'''
student_att = int (input("pls enter your same attendance: "))
if student_att >=75:



student_marks = int (input("Enter your marks: "))
if student_marks >= 90:
    print("you got A+ grade")
elif student_marks >= 75 and student_marks <90:
   print ("you got A grade")
elif student_marks >= 60 and student_marks <75:
    print (" you got B grade")
else:
    print ("your fail")


num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
usre_choice = input("Enter your choice: ")
if usre_choice == "+":
    print (num_1+num_2)
elif user_choice == "-":
    print (num_1-num_2)'''

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
user_choice = input("Enter your choice \n1.add \n2.sub \n3.mul \n4.div ")
if user_choice == "+":
    print(num_1 + num_2)
elif user_choice == 2:
    print(num_1 - num_2)
elif user_choice == 3:
    print(num_1 * num_2)
elif user_choice == 4:
    print(num_1 % num_2)
