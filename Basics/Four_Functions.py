# def hello():
#     print('Howdy!')
#     print('are you?')
# hello()
# hello()

# def hello(name):
#     print("Hey,"+ name)
#     print("how are you?,"+name)
# hello('Alice')
# hello('Sweety')

# def getValue(income):
#     if income<=10000:
#         return 'Income is 10k'
#     elif income>10000:
#         return 'Income is more than 10K'
# income=int(input())
# value=getValue(income)
# print(value)

# #the None Value
# spam=print("Hello!")
# if spam==None:
#     print("True")

# print('cats','Dogs','Mice',sep=',')

# #------------------------------Global Varable can be accessable with any scope
# def add(a,b):
#     return a+b
# a=1
# b=2
# sum=add(a,b)
# print(sum)

# #-----------------------------Local Varable/Value can be accessbale within the scope
# import random
# def value(a):
#     a=random.randint(1,10)
# a=100
# value(a)
# print(a)

# #-------------------------------You can mention global varables within local scope using global keyword
# def spam():
#     global eggs
#     eggs='spam'
# eggs='global'
# spam()
# print(eggs)


#Local Varables cannot be used in the global scope
#Local scopes cannot use variables in other local scopes
#Global variables can be read from a local scope
#Local and Global vrables with the same name


# #--------------------Exception Handling
# def div(value):
#     try:
#         return 42/value
#     except ZeroDivisionError:
#         print("Error: Invalid Argument.")
# print(div(2))
# print(div(5))
# print(div(0))
# print(div(1))

#import time, sys
#time.sleep(1) #pause for 1/10 of a sec

#----------------------------------------The Collatz Sequence

def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1
print("Enter a Number: ")
number=input()
while True:
    try:
        number=collatz(int(number))
        print(number)
        if number==1:
            break
    except ValueError:
        print("Please Enter A number, not letters")
        break

