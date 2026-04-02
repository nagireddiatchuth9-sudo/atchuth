'''Brack---> this is used to exit from the loop, when  we found the required value...

for j in range(1,20):
    print (j)
    if j == 5:
        break

lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1:
        break

for j in range(1,10):
    if j == 5:
        continue
    print(j)

for n in lis_:
    if n == 2:
        continue
    print(n)

for j in range(1,100):
    pass
for m in range (1,10):
    print (m)
else:
        print("else block")

num = 1 
while num<5:
    print(num)

while --- this a conbination for and if statement, if we did not end the loop in properway it will
run upto the memopry space in the become empty'''

user_in = int(input("enter the limit"))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")




