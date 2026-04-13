'''generators
-------------
this is a special type of function that return as
ITERATOR which one at a time
 
yield
-----
-->this is used to produce a value and pause execution

Next()
--->this is used to get next value from a generator
--->when the value is finished, it will stop the iterator


def my_generator():
    yield 1
    yield 2
    yield 3

an = my_generator()

print(next(an))
print(next(an))
print(next(an))


def square_gen(n):
    for i in range(n):
        yield i*i
 
for val in square_gen(15):
    print(val)'''

def square_gen(n):
    for j in range(n):
        yield 58*69

for val in square_gen(18):
    print(val)



















