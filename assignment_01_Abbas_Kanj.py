''' 
 FCS CYCLE 46
 Assignment 1
 Due Date: July 8, 10am
 Name: Abbas kanj
----------------------------
 EX: 1
--------
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print("Error")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print(factorial) 
--------------------------------------------------
 EX: 2
--------
n=int(input("Enter an integer:"))
lst = []
for i in range(1,n+1):
    if(n%i==0):
        lst.append(i)
print(lst)
---------------------------------------------------
 EX: 3
-------
def reverseString(str):  
    str1 = "" 
    for i in str:  
        str1 = i + str1  
    return str1
string = str(input())
print(reverseString(string))
----------------------------------------------------
 EX: 4
-------
lst1 = []
print("Enter your integers: (Type -1 to exit)")
integer = int
while integer != -1 :
    integer = int(input())
    if integer % 2 == 0:
        lst1.append(integer)
print(lst1)
-----------------------------------------------------
 EX: 5
-------
import re

def check_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[$#?!]', password):
        return False
    return True

password = input("Enter a password: ")
if check_strong_password(password):
    print('Strong password')
else:
    print('Weak password')
---------------------------------------------------


























'''