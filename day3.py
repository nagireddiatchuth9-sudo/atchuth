'''
operator --> operator is a symbol that pereform an operator on one or more value (operators) and produce result
operstor are primaily used :
--> Caculate value
--> Compare value / input
-->Make decision
-->Control the program flow
there are major seven categories of operators in python
-->Atithmetic operators
-->Assingment operators
-->Comparshipe operators
-->Membership operatos (in,not in)
-->Identity operators (is,is not)
-->Bitwise operators
-->Logical operators (and,or,not)
'''

'''
#Arithmetic Operators -->Aritmetic Operators perform mathematic operators

# + -->Addition,- -->Subtraction , * -->Muliplication, / -->Division
# ** -->Exponet , % -->modulus,//>intrger Devision

a=5
b=5
print (a+b)
print (a-b)
print (a*b)
print (a/b) #returns the result in float value
print(a**b) #returns the exponential value

print (a % b) #modulus division -->returns remainder
print (a // b)#Flooring / integer Division --> returns Quotient discrads

num1 = int (input("Enter the first value:"))
num2 = float(intput("Enter the second value:"))
result = (num1 + num2)*4
print (" the result is",result) #standard   notation

# f-string notation
print (f'the result is {result}')
print (f' the result of {num1} ane {num2} is {result}, {num1*num2}')


#Assignment operators
#--> = Assign, Additioin Assignment ,
#-=--> Subtract Assignment,*=,/=,%=,//,=,**=

# they are major used for code repetitions in applation usage

a=4
b=3
a +=2 #--> a=a+2
print (a)
b +=b
print (b)
#in similar way check for -=, *=, **,/=, %=, //=

b-= 3 #b = b-3
print (b)
print (f' the update velues of and b are {a} {b}')
b*= a # b = b*a
print (b)

'''
'''
# relational or comparision operators --> they always return the boolean
# value (true / fales)

#== is equal to, != not equals to
#<less than,>greater then , >=,<=

a = int(input("Enter a value :"))
b = int(input("Enter another value:"))
print (a==b)
print (a!=b)
print (A<b)
print (a>b)
print (a<=b)
print (a>=b)
'''

'''
#mambership operators --> they check for the existance of an object in a
#collcation --> int,not in

a = "codgnan"
print (type (a))
print ('a' in a)
print ('z' not in 'atchuth')
print ('z' not in 'codegnan')

b = [12,6,3,4]
c = int(input("Enter the value"))
print (C)
print (c in b)
print (c not in b)
'''
'''
# Logical operators -->they  are used to combine multiple conitions
#and ,or,not

age = int(input("Enter the age :"))
vote_right = true

print (age>=18 and vote_right) #both condition to be true then only true
print (age>18 or vote_right) #any one condition is true then result is true
print (not vote_right)
'''
'''
#Identity operators -->they check the memory location and validate we use
#(id) funcation it is different from == operator ->is,is not

a = [1,2,4]
b = [1,2,4]
print (a == b)
print (id(a)) #returns the identity of an object
print (id(b))
print (a is b)
print (a is not b)

c = b
print (c)
print (id(c))
print (c is b)
'''
#Bitwise operators -->Bitwise and & ,Bitwise OR perform bitwise operators
#we get teh result(remember the binary coversion)
print (5&3)
print (bin(5)) #returns binary number
