#Determines if the regex matches at beginning of the string

import re
text = "Welcome to DevOps World"
pattern = r"Welcome"
result = re.match(pattern, text)
print(result)