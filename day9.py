'''prime_num = int(input("enter a number:"))
count = 0
for j in range(1,prime_num+1):
        print(j)
        if prime_num % j == 0:
                count += 1
                print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{print_num} is not a prime number")

for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
    if count == 5:
        print(f"{an} is a prime number")
    else:
        print(f"{an} is not a prime number")

lis = [1027,197,9,86,17673]
for j in  lis:
    count = 0
    for i in range(1,j+1):
        if  j% i== 0:
            count +=1
    if count == 2:
        print(f"{j} is a prime number")
    else:
        print(f"{j} is not a prime number")'''


any = [12,356,8,6,2,8]
empty_ = []
for j 	in any:
    if j not in empty_:
        empty_.append(j)
print(empty_)











