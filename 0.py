#!/usr/bin/env python3
import math

url = "http://www.pythonchallenge.com/pc/def/0.html"
maths = str(int(math.pow(2, 38)))
new_url = url.replace("0",maths)

print(new_url)
