#Function for Addition

def add(a,b):
    return a+b

#Function for Subtraction

def sub(a,b):
    return a-b

#Function for Division

def div(a,b):
    return a/b

#Function for Multiplication

def mul(a,b):
    return a*b

#Calling the Function and storing the values

Addition = add(5, 7)
Subtraction = sub(5,7)
Division = div(10, 2)
Multiplication = mul(5,2)

print(f"The Sum is: {Addition}")
print(f"The Sub is: {Subtraction}")
print(f"The Div is: {Division}")
print(f"The Mul is: {Multiplication}")

#Another Method Calling the Function 

a = 20
b = 10

print (f"Addition of {a} + {b} = {add(a, b)}")
print (f"Subtraction of {a} - {b} = {sub(a,b)}")
print (f"Division of {a} / {b} = {div(a,b)}")
print (f"Multiplication of {a} * {b} = {mul(a,b)}")
