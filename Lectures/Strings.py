'hello'
"world"
"This is also a string"
"I'm going on a run"

# escape sequences lead with backslash: 
# \n new line 
# \t tab 
# len() allows to check length of string
"hello \nworld"


# String in double or single quotes, prefer double
# strings are ordered sequences
# can use indexing and slicing to grab sub-sections of the string
# indexing notation uses [] after the string (or variable assigned the string)
# indexing allows you to grab a single character from the string

# These actions use square brackets and a number index to indicate positions of what you wish to grab
# Character:    h e l l o
# Index:        0 1 2 3 4 
# Reverse Index:0 -4 -3 -2 -1

mystring = "Hello World"
# H
mystring[0]
# R
mystring[8]
# R
mystring[-3]

# Slicing allows you to grab a subsection of multiple characters, a "slice" of the string.
# Syntax: [start:stop:step]
# start is a numerical index for the slice start
# stop is the index you will go up to (but not include) 
# step is the size of the "jump" you will take

mystring = "abcdefghijk"
# to end
mystring[2:]
# everything up to index, stop index goes up to but not including index position
mystring[:3]
# section of string
mystring[3:6]
# step size all from beginning to end with step size of 2
mystring[::2]
# reversing a string
mystring[::-1]

# String properties and methods

# Immutability: strings/string variables can't be reassigned
# concatenation: can't concatenate numbers with strings
x = "HelloWorld"
x + " it is beautiful outside"
letter = "z"
letter * 10

# String methods
x = "Hello World"
x.upper()
x.lower()
# split string into list
x = "Hi this is a string"
x.split("i")

# Print formatting with strings
# often you will want to "inject" a variable into your string for printing. 
# called string interpolation
# .format() method
print("this is a string {}".format("Inserted"))
print("the {2} {1} {0}".format("fox", "brown", "quick"))
print("the {q} {b} {f}".format(f="fox", b="brown", q="quick"))
# float formatting "{value:width:precisionf}"
result = 100/777
print("The result was {r:1.3f}".format(r=result))
# f-strings: formatted string literals
name = "Nick"
print(f"Hello, his name is {name}")


