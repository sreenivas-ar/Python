"""print("Enter Your Income with paises")
income=float(input())
print("Your Monthly Income is "+str(income))
income=int(income)
print("Your income in numbers is " +str(income))
if income < 10000 :
    print("You are in below poverty line")
elif (income >=10000 and income<=30000):
    print("You are in mid line")
else:
    print("You are okay in line")
"""

# #Annoying while loop
# name=''
# while name!='Your Name':
#     print("Enter Your Name : ")
#     name=input()
# print("Thank You")

# while True:
#     print("Enter Your Name : ")
#     name=input()
#     if name=='Your Name':
#         break
# print("Thank You")

# #sum of n numbers using for loop
# #By Default i starts from 0 and will add upto n, <n
# print("Enter a number")
# n=int(input())
# sum=0
# for i in range(n+1):
#     print(i)
#     sum=sum+i
# print("Sum of n Numbers: "+str(sum))

# sum=0
# for i in range(1,n):
#     sum=sum+i
# print("Sum of n numbers: "+str(sum))

# #sum of  even numbers between 2 to n
# sum=0
# for i in range(2,n,2):
#     print(i)
#     sum+=i
# print("Sum of Even Numbers till n :"+ str(sum))

# #for i in range(start,end,step)


# for i in range(5,-1,-1):
#     print(i)

# #importing Modules
# import random
# for i in range(5):
#     print(random.randint(1,10))

#import random, sys, os, math

#from random import *

# import sys
# while True:
#     print("Type E for Exit and N for not to exit the code")
#     res = input()
#     if res=='E':
#         sys.exit() #this will close/terminate the program with exit()
#     elif res=='N':
#         print("Going to loop next")


#print('%s Wins %sLosses %s Ties' %(wins, losses, ties))

#------------------------------------------------------------------------------
#---------------------Practice Questions---------------------------------------

# #Question 9
# spam=int(input())
# if spam==1:
#     print("Hello")
# elif spam==2:
#     print("Howdy")
# else:
#     print("Greetings")


# #Question 13
# i=1
# while(i<=10):
#     print(i)
#     i+=1


#round() and abs() Returns the absolute value (non-negative distance from zero) of a number.
#Rounds a number to a specified number of decimal places (rounds half to even by default).

# number = 3.14159
# rounded_two_decimals = round(number, 2)
# print(rounded_two_decimals)  # Output: 3.14
