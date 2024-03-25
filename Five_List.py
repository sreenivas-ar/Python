spam=['cat','Dog','Monkey','elephant']
print(spam)
print('0 is '+spam[0])
print('-1 is '+spam[-1])
print(spam[:])
print(spam[:3])
print(spam[2:])
print(spam[1:3])
print(spam[:-1])
print(str(len(spam)))
del spam[0]
print(spam)
if 'Dog' in spam:
    print(spam.index('Dog'))
else:
    print("There is no  Dog")
if 'cat' not in spam:
    print("Cat was removed  from the list.")
spam=spam+['cat', 'fish', 'Donkey']
print(spam)
print(spam*2)
print(spam+[1,2,3])
spam=[spam, ['Bow', 'Meow', 'kuku']]
#spam=[['Dog', 'Monkey', 'elephant', 'cat', 'fish', 'Donkey'], ['Bow', 'Meow', 'kuku']]
print(spam[0][1])
spam=spam[0][0]+' '+spam[1][0]
print(spam)
spam=['cat','Dog','Monkey','elephant']
#spam.append('Aardvark')
print(spam)
spam[3]='donkey'
print(spam)
#spam.insert(3,'Zebra')
#spam.remove('Dog') #if the value exist in multple places, it will remove only the first occorance
for i in range(len(spam)):
    print(spam[i])
for index, animal in enumerate(spam):
    print(animal)

import random
print('choice is '+random.choice(spam))

print(spam)
print('before shuffle')
random.shuffle(spam)
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spam.sort(key=str.lower)
print(spam)
spam.reverse()
print(spam)

#-----------------------------Strings------------------------------------------------------

name='Salma'
print(name[0] + ' loves ' + name[0])
print(name[1:])
print(name[:4])
print(name[1:4])
if 'S' in name:
    print(name,end=" ")
    name='Sreenivas'
    print(' loves ' + name)
for i in name:
    print(i,sep="-")

#list are mutable, can be changed like append, remove, changed but string is immutable, cannot be changed

#---------------------------------------------Tuples------------------------
eggs=('hello', 42, 0.5)
print(eggs)

#tuples are immutable

print(('animal',))
print(('hello'))

#converting
print(list(name))
print(list(eggs))
animal=['cat','dog','moneky']
print(tuple(animal))

#referance
spam=['cat','Dog','Monkey','elephant']
animal=spam
print(animal)
animal[3]='Donkey'
print(spam)

#id function id()
print(id(name))

#passing referance
def update_list(lst):
    lst.append("Python")
list=['Java','C++']
update_list(list)
print(list)

#call by object - pass the list as an argument and then modify it using methods of

#copy module
import copy
spam=['A','B','C']
print(id(spam))
spam1=copy.copy(spam)
print(id(spam),id(spam1))
spam1.append('D')
print(spam,spam1)
print(id(spam1))
#deepcopy method
spam2=copy.deepcopy(spam)
print(id(spam))
print(id(spam2))
spam2.append('E')
print(spam,spam2)
