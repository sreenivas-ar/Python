myStudent={'name':'Sreenivas', 'class':'11', 'group':'MPC'}
print(myStudent['name']) # Accessing the value of name key in dictionary

print(list(myStudent.keys()))  # Returns a list of all available keys in the dictionary
print(list(myStudent.values()))# Returns a list of all values in the dictionary
print(list(myStudent))

for i in myStudent.keys():
    print(i)
for i in myStudent.values():
    print(i)
for i in myStudent.items():
    print(i)

for k,v in myStudent.items():
    print("Value "+k+" is "+ str(v))

#checking the key or value is in dictonary
if 'name' in myStudent.keys():
    print("value exist")

#get() method
print("hello, age: "+str(myStudent.get('age',17))+ " : " +myStudent['name'])

#setdefault() Method
myStudent.setdefault('sno','1')
print(myStudent)
myStudent.setdefault('sno','12')
print(myStudent)

import pprint
pprint.pprint(myStudent)   # pretty printing
print(pprint.pformat(myStudent))