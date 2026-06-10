print("program starts")
a=10
print("a=",a)
try:
    print("result=",a/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")        
print("program ends")
#'''
# '''
age=int(input("enter the age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")