


'''What are strings?

Strings are sequences of characters used to represent text in Python.
They're essential for storing and manipulating various text-based data like names, messages, addresses, code snippets, and more.
Key characteristics:

Immutable: Once created, you cannot modify the characters within a string directly. Operations on strings typically create new strings.
Enclosed in quotes: You can use either single quotes (') or double quotes (") to create strings.
Unicode support: Python strings support a wide range of characters from different languages and scripts, making them versatile for international text.

Common string methods:

upper(): Converts all characters to uppercase.
lower(): Converts all characters to lowercase.
split(): Splits a string into a list of substrings based on a delimiter.
join(): Joins a list of strings into a single string using a separator.
find(): Returns the index of the first occurrence of a substring.
replace(): Replaces occurrences of a substring with another string.
strip(): Removes leading and trailing whitespace characters.
'''


mystr1='Welcome'
print(mystr1)
mystr2="Welcome"
print(mystr2)
mystr3='''Welcome'''

mystr3="""Welcome
to the world of
python programming"""
print(mystr3)

mystr='language'
print('mystr = ',mystr)
print('mystr[0] = ',mystr[0])
print('mystr[-1] = ',mystr[-1])
print('mystr[1:5] = ',mystr[1:5])
print('mystr[5:-2] = ',mystr[5:-2])

mystr='language'
print(mystr)
mystr='programming'
print(mystr)

mystr1='Welcome'
mystr2=' to all'
print('mystr1 + mystr2 =',mystr1 + mystr2)
print('mystr1*3 = ',mystr1*3)

letter_count=0
for letters in "Hello World":
    if(letters=='l'):
        letter_count+=1
print(letter_count,'times l letter has been found')

print('l' in 'hello')
print('l' not in 'hello')
print('b' in 'hello')
print('b' not  in 'hello')

mystr="university"
my_list_enumerate=list(enumerate(mystr))
print('list(enumerate(mystr))',my_list_enumerate)
print('len(mystr) = ',len(mystr))

print('''tell me "what's your name?"''')
print('tell me "what\'s your name?"')
print("tell me 'what's your name?'")
print("tell me \"what's your name?\"")

print("C:\\User\\user\\mydata.txt")
print("this line is having a new line \ncharacter")
print("this line is having a tab \t character")
print("ABC written in\x42\x42\x43 (HEX) representation)")

default_order="{} {} and {}".format('Today','is','Sunday')
print(default_order)

positional_order="{1} {0} and {2}".format('is','today','Sunday')
print(positional_order)

keyword_order="{t} {i} and {s} ".format(i='is',t='today',s='sunday')
print(keyword_order)

print("Required binary representation of {0} is {0:b}".format(20))
print("Exponenet reprsentation :{0:e}".format(1566.345))
print("One third is:{0:.3f}".format(1/3))

print("gOOD moRNing to alL".lower())
print("gOOD moRNing to alL".upper())
print("gOOD moRNing to alL".find('tO'))
print("gOOD moRNing to alL".find('to'))
print("gOOD moRNing to alL".replace('alL','everybody'))
print("gOOD moRNing to alL".replace('all','everybody'))