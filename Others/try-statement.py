# Exceptional handling

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement.

#Program Setup

import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    div = a/b
    print (div)
except ZeroDivisionError:
    print("Error: Divisio by zero is not allowed")

    

