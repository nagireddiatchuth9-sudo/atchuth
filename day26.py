'''regular expression(reg ex)
----------------------------
-->this regular expression or regEx is a sequence of characters that forms a searching pattern.
--> to use this we have to import re,which will unlock the package

FUNCTONS
-----------
1.findall
-->by using this functon, it will find all sequence in the string
syntax-->re.findall(metacher,variable_name)
2.search
-------
-->by using this function ,it will only find first sequence in the string
syntax-->re.search ("metachar",variable_name)

metacharacters
---------------
-->metacharacters are used to form searching pattren
1.[]
----
--> in this meta character we can search for [a-z], [A-Z], [0,9]
 

import re
any  = "this method can read entair file and return into list with"
so =re.findall("[a-z]", any)
an =re.search("[a]",any)
print (so)

import re
some  = "by using this functon, it will find all sequence in the string"
an =re.search("[a]",some)
print (an)

2.dot(.)
-->this meta character will from a searching patter as is will take any single character for(.)ot

import re
we = "hello"
the = re.findall("h...o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

import re
we = "atchuth"
the = re.findall("a....th",we)
thing = re.search("a....th",we)
print(the)
print(thing)


3.^
---
-> this  is use to find the string in starting with the sequence or

syntex--> re.finall("metachar",variable_name)

import re
want = re.findall ("^this " , we)
print(want)


4.$
this is used to find the string is ending with the sequence or not

syntax--> re.findall("$",variable_name)

import re
out = "this is used to find the string is ending eith the sequence"
one = re.findall("sequence $",out)
two =re.search("this $", out)
print(one)
print(two)


5.*
---
-->this meta character will from a searching pattern as it will take any zero or more character for (*)

import re
atchuth ="this meta character will from a searching pattern"
gk = re.findall("c.*i",atchuth)
nk = re.search("c.*i",atchuth)
print(gk)
print(nk)
 
6.+
---
-->this is meta character will from a searching pattern as it will take any one or more character for (+)

syntex --> re.search(".+",variable_name)
'''

import re
atchuth = "this meta character will from a searching pattern as it will"
gk = re.findall("an.+y",atchuth)
koll = re.search("t.+",atchuth)
print(gk)
print(koll)
















