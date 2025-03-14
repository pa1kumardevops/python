import re

text = "DevOps is a set of practices, tools, and the cultural philosophies that aim to automate and integrate the processes between software development (Dev) and IT operations (Ops)"

pattern = "the"

result = re.findall(pattern, text)

print(result)
