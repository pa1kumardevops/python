#Searches the string for a match and returns the first occurence

import re

text = "DevOps is a set of practices, tools, and the cultural philosophies that aim to automate and integrate the processes between software development (Dev) and IT operations (Ops)"

pattern = r"the"


result = re.search(pattern, text)

print (result)