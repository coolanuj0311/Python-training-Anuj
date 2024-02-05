'''Common methods for working with RegEx:

match(): Checks for a match at the beginning of a string.
search(): Searches for a match anywhere in the string.
findall(): Finds all non-overlapping matches and returns them as a list.
finditer(): Finds all matches and returns them as an iterator of match objects.
sub(): Replaces matches with a specified string.
split(): Splits the string at the occurrences of a pattern.

Accessing match information:

match.group(): Returns the matched text.
match.start(): Returns the start index of the match.
match.end(): Returns the end index of the match.

RegEx syntax:

Basic patterns:
. matches any single character.
\w matches any word character (letters, digits, underscores).
\d matches any digit.
\s matches any whitespace character.
^ matches the beginning of a string.
$ matches the end of a string.
Quantifiers:
* matches zero or more repetitions of the preceding pattern.
+ matches one or more repetitions.
? matches zero or one repetition.
{m,n} matches at least m and at most n repetitions.
Character classes:
[abc] matches any character within the brackets.
[^abc] matches any character not within the brackets.
Groups and backreferences:
(pattern) creates a group.
\1 refers to the first captured group.
'''
import re
if re.search("ape","The ape was at the apex"):
    print("There is an ape")
import re
allApes=re.findall("ape.","The ape was at the apex")
for i in allApes:
    print(i)

theStr="The ape was at the apex"
for i in re.finditer("ape.",theStr):
    locTuple=i.span()
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])

animalStr="Cat rat mat fat pat"
someAnimals=re.findall("[Crmfp]at",animalStr)
for i in someAnimals:
    print(i)

animalStr="Cat rat mat fat pat"
someAnimals=re.findall("[c-mC-M]at",animalStr)
for i in someAnimals:
    print(i)

animalStr="Cat rat mat fat pat"
someAnimals=re.findall("[^Cr]at",animalStr)
for i in someAnimals:
    print(i)

import re
owlFood="rat cat mat pat"
regex=re.compile("[cr]at")
owlFood=regex.sub("owl",owlFood)
print(owlFood)

import re
randStr="Here is \\stuff"
print("Find \\stuff:",re.search("\\stuff",randStr))
print("Find \\stuff:",re.search("\\\\stuff",randStr))
print("Find \\stuff:",re.search(r"\\stuff",randStr))

import re
randStr="F.B.I. I.R.S. CIA"
print("Matches:",len(re.findall(".\..\..",randStr)))
print("Matches:",re.findall(".\..\..",randStr))

import re
randStr="""This is a long
string that goes
on for many lines
"""
print(randStr)

regex=re.compile("\n")
randStr=regex.sub(" ",randStr)
print(randStr)

import re
randStr="12345"
print("Matches :",len(re.findall("\d",randStr)))

import re
if re.search("\d{5}","12345"):
    print("It is a zip code")
numStr="123 12345 123456 1234567"
print("Matches :",len(re.findall("\d{5,7}",numStr)))

import re
phNum="412-555-1212"
if re.search("\w{3}-\w{3}-\w{4}",phNum):
    print("It is a phone number")
if re.search("\w{2,20}","Ultraman"):
    print("It is a valid name")

import re
if re.search("\w{2,20}\s\w{2,20}","Toshio Muramatsu"):
    print("It is a valid full name")

import re
print("Matches :",len(re.findall("a+","a as ape bug")))
print("Matches :",re.findall("a+","a as ape bug"))

import re
emailList="db@aol.com m@.com @apple.com db@.com"
print("Email Matches :",len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",emailList)))

print("Email Matches :",re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",emailList))






