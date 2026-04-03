'''num = int(input("enter the limit: "))
for j in range(num):
    for i in range(j):
        print("i",end = "")
    print()

num = int(input("enter the limit: "))
for i in range(num -1,-1,-1):
    for j in range(i):
        print("*",end = "")
    print()

num = int(input("enter the limit: "))
for i in range(num):
        print(" " *(num-i),end = "")
        for j in range(i+1):
           print("*", end= " ")
        print()'''

sbi_atchuth_ = {"name" : "atchuth",
                "atm pin" : "9949",
                "balance" : 10000}
user_pin = input("enter 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in sbi_atchuth_['atm pin']:
        user_choice = int(input("enter  \n1. withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw "))
            if money_w <= sbi_atchuth_['balance']:
                sbi_atchuth_['balance'] -= money_w
                print(sbi_atchuth_['balance'])
            else:
                print("insyfft")
    else:
           print("invalid")


else:
        print("pls enter 4 digit pin")
