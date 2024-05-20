import os
import re

dir = "<abolute Path>"
pattern = "<Pattern>"

files = [f for f in os.listdir(dir) if re.match(pattern, f)]

for x in files:
    y = x.replace(pattern, '')
    print(y)
    os.rename(os.path.join(dir, x), os.path.join(dir, y))