'''lambda function()
-------------------
--> this is also called anonymous function..
--> a lambda function can take n number of argumaent but have only
one expression

synatax
------
   lambda(keyword) argu
ment : expression

any = lambda so : so + 10
print(any(6))

some = lambda an, how, do : (how - an)* do
print(some(4,9,2))


many = lambda an, do, then : (do - then)* an
print(many(5,4,2))

list comprehension
------------------
--> this is offers the shorter syntax when you want ti create a new list from the existing list

syntax
------
    variable_name = [expression loop and andition]


old_list = [1,2,3,4,5]
new_list = [j for j in old_list]
print(new_list)

old_list = [5,9,6]
new_list = [j for j in  old_list if j % 5!=0]
print(new_list)


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
                print(sbi_atchuth_['balance'])'''






















   
