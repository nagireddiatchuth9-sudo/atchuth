 file Handling---> fille handler is an object of file to maintain several functions of file such as creating,   
reading, writing and update also deleting the file
How to open a file
1. open()--->This open ()function takes 2 parameters and in this we have to close the file by calling close() function after program..
1file name
2mode

2.with open()
modes("r","w","a","x","t")
1."r"--read
to read the file we will use this mode and if the file doesn't exist,it troughs the error

some=open("dummy.txt","r")
print(some.read())
some.close()

2."w"--write
to write the text into the file we will use this mode and it will create the file if it doesn't exist

any=open("dummy.txt","w")
any.write("I'm learning python")
any.close()


3."a"--append
to add the text into the file this is used and it will create the file if it doen't exist
'''
any=open("dummy.txt","a")
any.write("this is line 4")
any.close()



















