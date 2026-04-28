'''7.?
---
--> this is character will from a searching pattern as it will take any zero or one character for(?)
syntex--> re.findall(".?", variable_name)

import re
any = "this meta character will from a searching pattern as it will take any zero or one character for (?)"
an = re.findall(".this?",any)
print(an)

8.{}
----
-->this meta character will from a searching pattern as we can mention the size in the {}
syntex--> re.search(".{size}",variable)

import re
any = any = "this meta character will from a searching pattern as it will take any zero or one character for (?)"
an = re.findall("met.{50}?",any)
print(an)



9.|
---
-->this meta character will from a searching pattern as it consider right or lift any string is present
or not for(|)

import re
any = "this meta character will from"
an = re.findall("that|will",any)
print(an)

special sequence
----------------
A special sequence is a \ followed by one of the character in the list below, and has a

special meaning

\A
---
Returns a match if the specified character are at the beginning of the 
string
EG: "\Athe"
import re
txt = "the rain in spain"
#check if the string starts with "the":
x = re.findall("\Athe", txt)
print(x)
if x:
    print("yes, there is a match!")
else:
    print("no match")


\b-Returns a match if the specified character are at the beginning or at the end of a word
Eg: r"\bain"

import re
txt = "the rain in spain"
#check if " is present at the beginning of a WORD:
x = re.findall(r"\bspain",txt)
print(x)
if x:
    print("yes, there is a match")
else:
    print("no match")


\d- Returns a match where the string contains digit(number from0-9)
Eg: "\dell"

import re
txt = "the rain in 56 spain"
#check if is string  contains any digit
x = re.findall(r"\D",txt)
print(x)
if x:
    print("yes this is a match")
else:
    print("no match")

\D- Returns a match where the string DOES NOT contains digits
Eg: "\D"

import re
txt = "the rain in 58 spain"
#check 
x = re.findall(r"\D",txt)
print(x)
if x:
    print("yes, there is at least one match!")
else:
    print("no match")

 
\S- Returns a match where the string  contains a whait space character
Eg: "\s"

import re
txt = "the rain in  spain"
#Return a match at every whit-space character:
x = re.findall(r"\s", txt)
print(x)
if x:
    print("yes, there is at least one match!")
else:
    print("no match")


")

 
\S- Returns a match where the string DOES NOT contains a whait space character
Eg: "\s"

import re
txt = "the rain in  spain"
#Return a match at every  NON whit-space character:
x = re.findall("\S", txt)
print(x)
if x:
    print("yes, there is at least one match!")
else:
    print("no match")


Time amd Date
------------
%d-------> day
%m-------> month
%y-------> year
%h-------> hours
%m-------> min
%s-------> sec
%p-------> AM/PM
%a-------> day name
%b-------> month name'''

import datetime
now= datetime.datetime.now()
print(now)

import datetime
today = datetime.date.today()
print(today.strftime("%d-%m-%y"))
print(today.strftime("%A"))
print(today.strftime("%b"))
































