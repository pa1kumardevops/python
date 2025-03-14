# import re

# text = "DevOps is a set of practices, tools, and the cultural philosophies that aim to automate and integrate the processes between software development (Dev) and IT operations (Ops)"

# pattern = r"DevOps"

# replacement = "The DevOps"

# result = re.sub(pattern, replacement, text)

# print(result)

import re
result = re.search(r'\d+', 'There are 123 apples')
print(result.group())
