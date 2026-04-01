'''table_num = 19
for j in range(1,10):
    print(f"{table_num} x {j} = {tab le_num * j}")

an = "python is a programming languane"
count_u = 0
count_l = 0
for ch in an:
    if ch.isupper():
        count_u += 1
    elif ch.islower():
print(f"there are total {count_u} cap l")
print(f"there are total {count_l} small l")

an = "python is a programming language"
Cap_l = []
small_l = []
for ch in an:
      if ch.isupper():
            Cap_l.append(ch)
      elif ch.pin():
             small_l.append(ch)
print(f"{Cap_l} contain all cap l")
print(f"{small_l} contain all small l

sbi_atchuth_ac_details = {"name" : "atchuth",
                          "atm pin" : "9949"}
print("welcome to sbi atm")
print("pls insert your atm card")
sbi_user_pin =  input("pls enter your 4 digits pin:")
if len(sbi_user_pin) == 4:
    if sbi_user_pin in sbi_atchuth_ac_details['atm pin']:
        print("the pin correct")
    else:
        print("you have entered invelid pin")
else:
    print("ls enter 4 digit pin")'''


per_num = int(input("enter a number: "))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the prefact num")
else:
    print("{per_num} is not a prefact num")















