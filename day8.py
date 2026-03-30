'''any_="python is a progaramming language"
vowel_cou= 0
space_cou = 0
con_cou
for j in any_:
    if j in"AEIOUaeiou":
        vowel_cou += 1
    elif j ==" ":
            space_cou += 1
 print(f"this is count of all vowel in the string{vowel_cou}")
 print(f"this is the count of all space in the string {space_cou}")
 print(f"this is count of all cons_in the string {len(any_)-(vowel_cou + space_cou)}")


a = 9
for j in range(2,10):
    print(j)
range()----> this ia used to generate number
syntex----> range(start,end,step)

for j in range(1,20,5):
    print(j)

any = "143"
print(int(any))
print(list(any))
print(tuple(any))


so = 158
print(str(so))
print(float(so))



an = [1,2,3]
va = str(an)
print(va)
print(tuple(an))
a = [(1,2),(3,4)]
print(dict(a))

rev_str = "vassu"
empty_ =""
for j in rev_str:
    empty_ = j + empty_
if empty_ ==rev_str:
    print(f"{rev_str} is palin")
else:
    print(f"{rev_str} is not a palin")'''

for num in range(1,58):
    if num % 2 == 0:
        print(f"{num} is a even num")
    else:
        print(f"{num} is a odd num")























