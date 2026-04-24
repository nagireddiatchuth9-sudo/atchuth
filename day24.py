'''#handling earrors
--------------
try block
-->the try block will test hte block of code for errors.
try:
    print(b)
except block
-------------
-->this block take any earrors
else block
finally block
-------------
--> this block will execute try block have any error or no error

try:
    a = 8
    b = 12
    print(a + b)
except:
    print("error here")
else:
    print("no error in the code")
try:
    atchuth = 21
    sharanya = 18
    print(atchuth + sharanya)
except:
    print("error here")
else:
    print("no error in the code")



try:  
    a = 8
    b = 12
    print(a + b)
except:
    print("error here")
else:
    print("no error in the code")
finally:
    print("the try-except block is finished")'''


try:
    num = int(input("enter number: "))
    num_2 = int(input("enter a number: "))
    result =- num / num_2
    print(f"result = {esult}")
except ValueError:
    print("pls enter a vaild number")
except NameError:
    print('erri')
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(f"result = {esult}")
finally:
    print(f"program is completed")




















    
    
