#spam='This is Sreeni's dad
spam="This is Sreeni's dad"
print(spam)

#Escape Characters
spam = "He said \"Hello\"."
print(spam)
spam='Women\'s Day'
print(spam)
print('Sreenivas\tloves\tSalma')
print("Cats\nDogs")
print('c:\\drive')

print(r'This is Sreeni\'s Life') #raw string

#Multiline string
print('''Animal
      is
      living thing''' )

"""   Multiple Comment Lines  """

#string inside other strings
name  = 'Sreeni'
age=23
print("My name is "+name+". I am "+str(age)+" years old.")
print('My name is %s and I am %s years old'%(name,age))
print(f'My name is {name} and i am {age} years old.') #f-strings  are used for formatting the text using variables.

print(spam.upper())
print(spam.lower())

if spam.islower():
    print("Everything is in lower case")
else:
    print(spam)

"""
islower()
isupper()
isalpha()
isalnum()
isdecimal()
isspace()
istitle()
startswith('Value')
endswith('Value')
join()
split()
"""

animal=['cat','dog','elephant']
print(', '.join(animal))
print(''.join(animal))
spam="This is Sreeni's dad"
print(spam.split(' '))

#partition()
print(spam.partition('i'))
before, sep, after = spam.partition(' ')
print(before)
print(after)

#rjust(), ljust(fillchar), center(width, fillchar).
name='salma'
print(name.ljust(8,"*"))
print(name.center(10,'$'))
print(name.rjust(20))

#removing white spaces strip(), rstrip(), lstrip()
phone_number="  9876543210      "
print(phone_number.strip())
print(phone_number.rstrip())
print(phone_number.lstrip())
print(phone_number.strip('90 '))

#chr(x) - gives ASCII value of character x and vice versa.
#ord(c) - gives Unicode code point for a one-character string c. 
print(chr(65)) #A
print(ord('A')) #65

import pyperclip
pyperclip.copy("Hello World")
pyperclip.paste()