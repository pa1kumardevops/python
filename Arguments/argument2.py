#Importing the sys Module
import sys

#Function for Addition and Multiplication

def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

# First check: Are enough arguments passed?
if len(sys.argv) < 4:
    print("❌ Operator not passed! 👇")
    print("Usage: python argument2.py <num1> <num2> <operator>")
    print("Example: python argument2.py 10 5 add")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operator = sys.argv[3]

addition = add(num1, num2)
multiplication = mul (num1, num2)

print(addition)
print(multiplication)

if operator == "add":
    output = add(num1, num2)
    print(output)
elif operator == "mul":
    output = mul (num1, num2)
    print(output)
else:
    print ("Please give the correct operator, it is like add, mul")
