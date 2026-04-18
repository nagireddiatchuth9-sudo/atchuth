'''constructor(_init_)
------------------
-->A constructor is a special method used initiallize object data
_inti_()

class student:
    def __init__(self,name,ID,day,batch):
        self.name = name
        self.ID = ID
        self.day = day        
    def display(self): 
        print(self.name, self.ID, self.day, self.batch)
stu1 = student("atchuth","2225014","15 days","01")
stul.display

Access specifier
1 . public
syntex----> name
we can use it anywhere in the program
2 . protected
syntex---->name
this is only for internal use
3 . private
syntex----> name
this one is restricted
self
--->this keywoed is instance variable and  unique for each object

class student:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"
any  = student()
print(any.public)
print(any.protected)
print(any.private)'''

# ATM Project - UBI Bank

SBI_atchuth_details = {
    "Name": "atchuth",
    "ATM_PIN":"9949",
    "Balance": 10000
}

print("Welcome to SBI ATM")
print("Please insert your ATM card")

# 🔐 3 Attempts for PIN
attempts = 3

while attempts > 0:
    user_pin = input("Enter your PIN: ")

    if user_pin == SBI_atchuth_details["ATM_PIN"]:
        print("✅ Login Successful")

        # 🔁 Menu Loop
        while True:
            print("\n1. Withdraw\n2. Deposit\n3. Change PIN\n4. Check Balance\n5. Exit")
            choice = int(input("Enter your choice: "))

            # Withdraw
            if choice == 1:
                amt = int(input("Enter amount: "))
                if amt <= SBI_atchuth_details["Balance"]:
                    SBI_atchuth_details["Balance"] -= amt
                    print(f"💰 Withdrawn Successfully. Balance: {SBI_atchuth_details['Balance']}")
                else:
                    print("❌ Insufficient Balance")

            # Deposit
            elif choice == 2:
                amt = int(input("Enter amount: "))
                if amt % 100 == 0:
                    SBI_atchuth_details["Balance"] += amt
                    print(f"💰 Deposited Successfully. Balance: {SBI_atchuth_details['Balance']}")
                else:
                    print("❌ Enter amount in multiples of 100")

            # Change PIN
            elif choice == 3:
                old_pin = input("Enter old PIN: ")

                if old_pin == SBI_atchuth_details["ATM_PIN"]:
                    new_pin = input("Enter new PIN: ")
                    confirm_pin = input("Confirm new PIN: ")

                    if len(new_pin) == 4 and new_pin == confirm_pin:
                        if new_pin != old_pin:
                            SBI_atchuth_details["ATM_PIN"] = new_pin
                            print("✅ PIN Changed Successfully")
                        else:
                            print("❌ New PIN cannot be same as old PIN")
                    else:
                        print("❌ PIN must be 4 digits and match")
                else:
                    print("❌ Wrong old PIN")

            # Check Balance
            elif choice == 4:
                print(f"💳 Current Balance:SBI_atchuth_details['Balance']")

            # Exit
            elif choice == 5:
                print("🙏 Thank you for using atchuth ATM")
                break

            else:
                print("❌ Invalid choice")

        break  # exit after successful session

    else:
        attempts -= 1
        print(f"❌ Wrong PIN! Attempts left: {attempts}")

        if attempts == 0:
            print("🚫 Your card is blocked")






























