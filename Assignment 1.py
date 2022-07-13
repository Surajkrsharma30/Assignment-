                                #ASSIGNMENT 01
                                #SURAJ KUMAR SHARMA
                                #DS29022B

#1.Build a calculator
#-------------------

#a=int(input("enter a number 1:"))
#operator=input("enter a operator(+,-,*,/):")
#b=int(input("enter a number 2:"))
#if operator=="+":
#    print(a+b)
#elif operator=="-":
#    print(a-b)
#elif operator=="*":
#    print(a*b)
#elif operator=="/":
#    print(a/b)
#else:
#   print("invalid operator")    

#2.program to calculate area of triangle
#--------------------------------------

#b=int(input("enter a base of a triangle:"))
#h=int(input("enter a height of a triangle:"))
#area_of_triangle=0.5*b*h
#print(area_of_triangle)

#3.swapping of two number
#------------------------

#a=10
#b=12
#a,b=b,a
#print(a)
#print(b)

#write a python program to convert kilometer to miles
#--------------------------------------------------------

#km=int(input("enter a number in kilometer:"))
#to_miles=km*1000
#print("converted  in miles:",to_miles)

#program to find square root of given number
#---------------------------------------------------------

#import math
#a=int(input("enter a number:"))
#b=math.sqrt(a)
#print(b)

#write a programme in python to find the largest number among the three numbers
#-------------------------------------------------------------------------------

#num_1=int(input("enter a number1:"))
#num_2=int(input("enter a number2:"))
#num_3=int(input("enter a number3:"))
#if num_1>num_2 & num_3:
#    print("num_1 is greater",num_1)
#elif num_1<num_2 & num_3:
#    print("num_2 is greater",num_2)
#else:
#    print("num_3 is greater",num_3)

#write a programme in python whether check number is prime or not
#----------------------------------------------------------------

a=int(input("enter a number:"))
if (a % 2 == 0):
    print("number is not prime")
else:
    print("number is prime")