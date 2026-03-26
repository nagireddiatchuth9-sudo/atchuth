'''print(9+7)
print("python"+"language")
print([1,2] + [3,4])

concatennation
------------------
this ias nothing but, a (+) behavi
case-1
------
intergers--- this will act as addtion for the int

case-2
------
for orther data type (we have to use same type)this(+)
act as concatenation 

print([1,2,] + [3,4,])

tutple()----->
-------
is a collaction of different datatype and this is representes
by (), separated by (,)
eg...

thing = (1,"vassu",[12,13,],[6,7,])
print(thing)

num = 6
num_2 = 80
print(f"before swapping num ={num} and num_2={num_2}")
num, num_2 =num_2,num
print(f"after swapping num ={num} and num_2={num_2}")'''

leap_year = int(input("Enter year: "))
if (leap_year % 4 == 0 and leap_year % 100 !=0)or leap_year % 400 == 0:
    print(f"yes, {leap_year} is a leap year")

else:
    print(f"no, {leap_year} is not leap year")

