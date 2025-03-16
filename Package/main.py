# Import the package (my_package)
import mypackage

# Use functions from the package

result_add = mypackage.add(3, 5)
result_subtract = mypackage.sub(10, 2)
result_upper = mypackage.to_upper("hello")
result_lower = mypackage.to_lower("WORLD")

print(f"Add: {result_add}")
print(f"Subtract: {result_subtract}")
print(f"Uppercase: {result_upper}")
print(f"Lowercase: {result_lower}")