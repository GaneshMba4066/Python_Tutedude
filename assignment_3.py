#Factorial of a number
x = int(input("Enter the Number:"))
def factorial(x:int)->int:
    if(x==0):
        return 1
    else:
        return x*factorial(x-1)
print(factorial(x))
#math library operations
import math
x = int(input("Enter the Number:"))
def m(x):
    print("Square Root:",math.sqrt(x))
    print("Logarithm: ",math.log(x))
    print("Sine :",math.sin(x))    
m(x)
