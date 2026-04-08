'''breaking it into smaller, simpler, subproblems.
Recursion is especially usefull for problems that can be
divided into identical smaller tasks, such as mathemetical

def validate_pin(self):
    while self.remaining_attemps > 0:
        usre_pain = input("enter 4 digit pin:")
        if len(user_pin) == 4 and user_pin == self.user_info:
            print("wlcome")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"inviled pin. attempts left:{self.remaining_attempts}")
            else:
                print(f"card blocked. please contact customer")
                return False

any = "python is language"
vowel_list = []
con_list = []
def vowel_con(any,vowel_list,con_list):
    for i in any:
        if i in "AEIOUaeiou":
           vowel_list.append(i)
        else:
            con_list.append(i)
    print(f"{vowel_list} these are all vowel in the string")
vowel_con(any,vowel_list,con_list)



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
                
            





















